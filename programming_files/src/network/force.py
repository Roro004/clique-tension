import numpy as np
from network.visuals import plot_graph
import matplotlib.pyplot as plt
from network.identify import map_nodes_to_cliques
import random
import math

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


    cliques = map_nodes_to_cliques(G)
    num_cliques = len(cliques)

    # for i in repulse_count:
    #     if repulse_count[i] > 2:
    #     # Only proceed if attractive forces exist
    #         for _, vector in force_vectors['attractive'].get((i, i), []):
    #         # Apply acceleration in the opposite direction only if nodes are in different cliques
    #             for j in repulse_count:
    #                 if j != i and map_nodes_to_cliques.get(i) != map_nodes_to_cliques.get(j):
    #                     displacement[i] -= vector * acceleration_factor





    # Assuming the desired range for x positions is between 0 and 1
    # Calculate equidistant x positions for each clique
    # x_positions = {clique: (index + 1) / (num_cliques + 1) for index, clique in enumerate(cliques)}

    # for i in repulse_count:
    #     if repulse_count[i] > 2:
    #         # Attract nodes to their clique's x-axis position
    #         clique_of_i = map_nodes_to_cliques.get(i)
    #         if clique_of_i is not None:
    #             target_x_position = x_positions[clique_of_i]

    #             # Assuming 'displacement' is a dict with node keys and (x, y) tuple values
    #             current_x, current_y = displacement[i]

    #             # Calculate the x-axis displacement needed to move towards the target x position
    #             # Adjust this calculation based on your specific needs (e.g., current position, fixed acceleration factor)
    #             x_displacement = (target_x_position - current_x) * acceleration_factor

    #             # Update the displacement with the new x value, leaving y as it is
    #             displacement[i] = (current_x + x_displacement, current_y)

    #             # If there are attractive forces, apply them as well
    #             for _, vector in force_vectors['attractive'].get((i, i), []):
    #                 for j in repulse_count:
    #                     if j != i and map_nodes_to_cliques.get(i) != map_nodes_to_cliques.get(j):
    #                         # Modify the x component of the vector only, as y is not fixed
    #                         displacement[i] = (displacement[i][0] - vector[0] * acceleration_factor, displacement[i][1])





    # for index, clique in enumerate(cliques):
    #         force_axis = 'x' if index % 2 == 0 else 'y'

    #         for node in clique:
    #             current_x, current_y = displacement[node]

    #             if force_axis == 'x':
    #                 # Apply force along the x-axis
    #                 x_displacement = acceleration_factor  # Adjust this for direction and magnitude
    #                 displacement[node] = (current_x + x_displacement, current_y)
    #             else:
    #                 # Apply force along the y-axis
    #                 y_displacement = acceleration_factor  # Adjust this for direction and magnitude
    #                 displacement[node] = (current_x, current_y + y_displacement)


    # cliques = list(set(map_nodes_to_cliques(G)))
    # num_cliques = len(cliques)
    # angle_increment = 360 / num_cliques  # Divide the circle into equal parts based on the number of cliques

    # for index, clique in enumerate(cliques):
    #     # Calculate the angle for this clique
    #     angle_degrees = index * angle_increment
    #     angle_radians = math.radians(angle_degrees)

    #     # Calculate the direction vector for this angle
    #     direction_x = math.cos(angle_radians)
    #     direction_y = math.sin(angle_radians)

    #     # Apply the force to each node in the clique
    #     for node in clique:
    #         current_x, current_y = displacement[node]

    #         # Calculate the new displacement
    #         new_x = current_x + direction_x * force_magnitude
    #         new_y = current_y + direction_y * force_magnitude

    #         displacement[node] = (new_x, new_y)




    return displacement, force_vectors







def update_positions(pos, displacement, cooling_factor=0.1):
    new_pos = {}
    for i in pos.keys():
        new_position = pos[i] + displacement[i] * cooling_factor
        if not np.all(np.isfinite(new_position)):
            new_position = np.random.rand(2)
        new_pos[i] = new_position
    return new_pos



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
