import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Circle

# Assume these functions are defined elsewhere in your module
from network.identify import map_nodes_to_cliques, find_max_cliques
from network.visuals import plot_graph

def initialize_positions(G):
    """Initialize node positions randomly."""
    return {i: np.random.rand(2) for i in G.nodes()}

def apply_forces(G, pos, repulsion=4000, attraction=0.1, attraction_factor=0.5, repulsion_factor=5000, max_displacement=10):
    """Apply forces based on current positions, returning displacement and force vectors."""
    displacement = {i: np.zeros(2) for i in G.nodes()}
    force_vectors = {'attractive': {}, 'repulsive': {}}
    cliques = find_max_cliques(G)

    clique_centroids = {}
    for idx, clique in enumerate(cliques):
        x_coords = [pos[node][0] for node in clique]
        y_coords = [pos[node][1] for node in clique]
        centroid = (sum(x_coords) / len(clique), sum(y_coords) / len(clique))
        clique_centroids[idx] = centroid

    # Apply attractive force towards their own centroid for each node in a clique
    for idx, clique in enumerate(cliques):
        centroid = clique_centroids[idx]
        for node in clique:
            vector_to_centroid = np.array(centroid) - np.array(pos[node])
            displacement[node] += vector_to_centroid * attraction_factor

    # Apply repulsion from other clique centroids
    for i, centroid_i in clique_centroids.items():
        for j, centroid_j in clique_centroids.items():
            if i != j:
                vector_between_centroids = np.array(centroid_i) - np.array(centroid_j)
                distance = np.linalg.norm(vector_between_centroids)
                if distance > 0:  # Avoid division by zero
                    repulsion_force = vector_between_centroids / (distance ** 2) * repulsion_factor
                    for node in cliques[i]:
                        displacement[node] -= repulsion_force

    return displacement, force_vectors

def update_positions(pos, displacement, cooling_factor=0.1):
    """Update positions based on displacement and cooling factor."""
    new_pos = {}
    for i in pos.keys():
        new_position = pos[i] + displacement[i] * cooling_factor
        if not np.all(np.isfinite(new_position)):
            new_position = np.random.rand(2)
        new_pos[i] = new_position
    return new_pos

def plot_graph(G, pos, cliques, ax):
    """Plot the graph, highlighting cliques and centroids."""
    ax.clear()
    nx.draw(G, pos, ax=ax, node_color='black', edge_color='gray', node_size=20, alpha=1)

    # Calculate and draw centroids for cliques
    for idx, clique in enumerate(cliques):
        x_coords = [pos[node][0] for node in clique]
        y_coords = [pos[node][1] for node in clique]
        centroid = (sum(x_coords) / len(clique), sum(y_coords) / len(clique))
        circle = Circle(centroid, 0.05, color='red', fill=True, alpha=0.6)
        ax.add_patch(circle)

def simulate(G, iterations=50, plot_every_n_steps=10, cooling_factor=0.95):
    """Run the simulation for a given graph G."""
    pos = initialize_positions(G)
    old_pos = pos.copy()
    fig, ax = plt.subplots(figsize=(8, 8))

    for iteration in range(iterations):
        displacement, force_vectors = apply_forces(G, pos)
        pos = update_positions(pos, displacement, cooling_factor)
        cooling_factor *= 0.95

        if iteration % plot_every_n_steps == 0 or iteration == iterations - 1:
            cliques = list(nx.find_cliques(G))
            plot_graph(G, pos, cliques, ax)
            ax.set_title(f"Iteration: {iteration}")
            plt.pause(0.1)  # Pause to observe each step
            old_pos = pos.copy()

    plt.show()

# Example usage:
# G = nx.karate_club_graph()  # Or any Graph you're working with
# simulate(G)
