import numpy as np
from network.visuals import plot_graph
import matplotlib.pyplot as plt
from network.identify import map_nodes_to_cliques
from graph_initializer import positive_edges, negative_edges

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

    for i in repulse_count:
        if repulse_count[i] > 2:  # Check if node i has more than 2 repulsive forces
            # Iterate over attractive forces, if they exist
            for j in G.nodes():
                if i != j and (i, j) in G.edges():
                    if (i, j) in positive_edges(G):  # Attract if positive edge
                        vector = force_vectors.get('attractive', {}).get((i, j), None)
                        if vector and map_nodes_to_cliques.get(i) != map_nodes_to_cliques.get(j):
                            displacement[i] += vector * acceleration_factor  # Attract towards node j
                    elif (i, j) in negative_edges(G):  # Repel if negative edge
                        vector = force_vectors.get('repulsive', {}).get((i, j), None)
                        if vector and map_nodes_to_cliques.get(i) != map_nodes_to_cliques.get(j):
                            displacement[i] -= vector * acceleration_factor  # Repel away from node j
        return displacement, force_vectors


# ----

    # clique_centroids = {}
    # for idx, clique in enumerate(cliques):
    #     x_coords = [pos[node][0] for node in clique]
    #     y_coords = [pos[node][1] for node in clique]
    #     centroid = (sum(x_coords) / len(clique), sum(y_coords) / len(clique))
    #     clique_centroids[idx] = centroid

    # # Apply attractive force towards their own centroid for each node in a clique
    # for idx, clique in enumerate(cliques):
    #     centroid = clique_centroids[idx]
    #     for node in clique:
    #         vector_to_centroid = np.array(centroid) - np.array(pos[node])
    #         displacement[node] += vector_to_centroid * attraction_factor

    # # Apply repulsion from other clique centroids
    # for i, centroid_i in clique_centroids.items():
    #     for j, centroid_j in clique_centroids.items():
    #         if i != j:
    #             vector_between_centroids = np.array(centroid_i) - np.array(centroid_j)
    #             distance = np.linalg.norm(vector_between_centroids)
    #             if distance > 0:  # Avoid division by zero
    #                 repulsion_force = vector_between_centroids / (distance ** 2) * repulsion_factor
    #                 for node in cliques[i]:
    #                     displacement[node] -= repulsion_force

    # return displacement, force_vectors












def update_positions(pos, displacement, cooling_factor=0.1):
    new_pos = {}
    for i in pos.keys():
        new_position = pos[i] + displacement[i] * cooling_factor


        # Ensure that the new position is finite, otherwise reset randomly
        if not np.all(np.isfinite(new_position)):
            new_position = np.random.rand(2)
        new_pos[i] = new_position
    return new_pos

def update_edge_weights(G, weight_increment=1):
    for u, v, d in G.edges(data=True):
        if d.get('weight', 0) > 0:
            d['weight'] += weight_increment  # Increase weight for positive edges
        elif d.get('weight', 0) < 0:
            d['weight'] -= weight_increment  # Increase weight for negative edges (make more negative)


def simulate(G, iterations=50, plot_every_n_steps=10, cooling_factor=0.95):
    pos = initialize_positions(G)
    old_pos = pos.copy()
    fig, ax = plt.subplots(figsize=(8, 8))

    for iteration in range(iterations):
        displacement, force_vectors = apply_forces(G, pos)
        pos = update_positions(pos, displacement, cooling_factor)


        if iteration % plot_every_n_steps == 0 or iteration == iterations - 1:
            plot_graph(G, pos, old_pos, force_vectors, ax)
            ax.set_title(f"Iteration: {iteration}")
            plt.pause(0.1)  # Pause to observe each step
            old_pos = pos.copy()

    plt.show()
