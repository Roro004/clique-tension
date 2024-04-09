import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from network.identify import find_max_cliques
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Circle

def plot_graph(G, pos, old_pos, force_vectors, cliques, ax):
    ax.clear()

    all_clique_nodes = set(node for clique in cliques for node in clique)
    all_nodes = set(G.nodes())
    non_clique_nodes = all_nodes - all_clique_nodes

    clique_centroids = {}
    for idx, clique in enumerate(cliques):
        x_coords = [pos[node][0] for node in clique]
        y_coords = [pos[node][1] for node in clique]
        centroid = (sum(x_coords) / len(clique), sum(y_coords) / len(clique))
        clique_centroids[idx] = centroid

        # Draw a red circle at the centroid
        circle = Circle(centroid, 0.1, color='red', fill=True, alpha=0.8)  # Increased size and opacity
        ax.add_patch(circle)

    colormap = plt.cm.get_cmap('Pastel2_r', len(cliques))

    # Increase linewidth for better visibility
    for idx, clique in enumerate(cliques):
        clique_color = colormap(idx / len(cliques))

        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                if G.has_edge(clique[i], clique[j]):
                    ax.plot([pos[clique[i]][0], pos[clique[j]][0]],
                            [pos[clique[i]][1], pos[clique[j]][1]],
                            color=clique_color, linewidth=3, alpha=0.7)

        centroid = clique_centroids[idx]
        for node in non_clique_nodes:
            for clique_member in clique:
                if G.has_edge(node, clique_member):
                    ax.plot([pos[node][0], centroid[0]], [pos[node][1], centroid[1]],
                            color='grey', linestyle='--', linewidth=2, alpha=0.8)
                    break

    # Draw nodes and edges with larger size for clarity
    nx.draw(G, pos, ax=ax, node_color='black', edge_color='gray', node_size=50, alpha=1)

    # Draw movement lines with increased visibility
    for i in pos.keys():
        if i in old_pos:
            ax.plot([old_pos[i][0], pos[i][0]], [old_pos[i][1], pos[i][1]], color='grey', linestyle='-', linewidth=2, alpha=0.7)

    # Enhance the visibility of force vectors
    for i, vectors in force_vectors['repulsive'].items():
        for j, vector in vectors:
            ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.005, alpha=0.7)

    for (i, j), vector in force_vectors['attractive'].items():
        ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.005, alpha=0.7)

    # Set limits to ensure all elements are within view
    ax.set_xlim(1.1 * np.min([pos[node][0] for node in G.nodes()]), 1.1 * np.max([pos[node][0] for node in G.nodes()]))
    ax.set_ylim(1.1 * np.min([pos[node][1] for node in G.nodes()]), 1.1 * np.max([pos[node][1] for node in G.nodes()]))
    ax.set_aspect('equal', adjustable='box')





    # Draw movement lines
    for i in pos.keys():
        if i in old_pos:
            ax.plot([old_pos[i][0], pos[i][0]], [old_pos[i][1], pos[i][1]], color='grey', linestyle='-', linewidth=1, alpha=0.5)

    for i, vectors in force_vectors['repulsive'].items():
        for j, vector in vectors:
            ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.002, alpha=0.5)

    for (i, j), vector in force_vectors['attractive'].items():
        ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.002, alpha=0.5)

