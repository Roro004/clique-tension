import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def initialize_positions(G):
    return {i: np.random.rand(2) for i in G.nodes()}

def apply_forces(G, pos, repulsion=4000, attraction=0.1, max_displacement=10, acceleration_factor=1.2):
    displacement = {i: np.zeros(2) for i in G.nodes()}
    force_vectors = {'attractive': {}, 'repulsive': {}}
    repulse_count = {i: 0 for i in G.nodes()}  # Count of repulsive forces for each node

    # Apply repulsive forces
    for i in G.nodes():
        for j in G.nodes():
            if i != j:
                delta = pos[i] - pos[j]
                distance = np.linalg.norm(delta) + 0.01
                force_magnitude = min(repulsion / distance**2, max_displacement)
                force_vector = delta / distance * force_magnitude
                displacement[i] += force_vector
                if i not in force_vectors['repulsive']:
                    force_vectors['repulsive'][i] = []
                force_vectors['repulsive'][i].append((j, force_vector))
                repulse_count[i] += 1  # Increment repulsive force count

    # Apply attractive forces
    for i, j in G.edges():
        delta = pos[i] - pos[j]
        distance = np.linalg.norm(delta)
        force_magnitude = min(distance**2 / attraction, max_displacement)
        direction = delta / distance
        force_vector = direction * force_magnitude
        displacement[i] -= force_vector
        displacement[j] += force_vector
        force_vectors['attractive'][(i, j)] = force_vector

    # Apply acceleration based on repulsive forces
    for i in repulse_count:
        if repulse_count[i] > 2:
            # Apply acceleration in opposite direction to attractive forces
            # Only if there are attractive forces acting on the node
            for _, vector in force_vectors['attractive'].get((i, i), []):
                displacement[i] -= vector * acceleration_factor

    return displacement, force_vectors

def update_positions(pos, displacement, cooling_factor=0.1):
    new_pos = {}
    for i in pos.keys():
        new_position = pos[i] + displacement[i] * cooling_factor
        if not np.all(np.isfinite(new_position)):
            new_position = np.random.rand(2)
        new_pos[i] = new_position
    return new_pos

def plot_graph(G, pos, old_pos, force_vectors, ax):
    ax.clear()
    nx.draw(G, pos, ax=ax, node_color='skyblue', edge_color='gray', node_size=50)

    # Draw movement lines
    for i in pos.keys():
        if i in old_pos:
            ax.plot([old_pos[i][0], pos[i][0]], [old_pos[i][1], pos[i][1]], color='grey', linestyle='-', linewidth=1, alpha=0.5)

    for i, vectors in force_vectors['repulsive'].items():
        for j, vector in vectors:
            ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.002, alpha=0.5)

    for (i, j), vector in force_vectors['attractive'].items():
        ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.002, alpha=0.5)

def simulate(G, iterations=50, plot_every_n_steps=10, cooling_factor=0.95):
    pos = initialize_positions(G)
    old_pos = pos.copy()
    fig, ax = plt.subplots(figsize=(8, 8))

    for iteration in range(iterations):
        displacement, force_vectors = apply_forces(G, pos)
        pos = update_positions(pos, displacement, cooling_factor)
        cooling_factor *= 0.95

        if iteration % plot_every_n_steps == 0 or iteration == iterations - 1:
            plot_graph(G, pos, old_pos, force_vectors, ax)
            ax.set_title(f"Iteration: {iteration}")
            plt.pause(0.1)  # Pause to observe each step
            old_pos = pos.copy()

    plt.show()

G = nx.karate_club_graph() # Example graph for demonstration
simulate(G, iterations=100, plot_every_n_steps=5)
