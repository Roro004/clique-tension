import matplotlib.pyplot as plt
import networkx as nx
from network.identify import find_max_cliques
import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(G, pos, old_pos, force_vectors, cliques, ax):
    ax.clear()

    # Assuming 'cliques' is a list of lists of node identifiers
    all_clique_nodes = set(node for clique in cliques for node in clique)
    all_nodes = set(G.nodes())
    non_clique_nodes = all_nodes - all_clique_nodes

    # Calculate centroids for each clique
    clique_centroids = {}
    for idx, clique in enumerate(cliques):
        x_coords = [pos[node][0] for node in clique]
        y_coords = [pos[node][1] for node in clique]
        centroid = (sum(x_coords) / len(clique), sum(y_coords) / len(clique))
        clique_centroids[idx] = centroid

    # Get a colormap
    colormap = plt.cm.get_cmap('Pastel2_r', len(cliques))

    # Highlight edges within and to cliques
    for idx, clique in enumerate(cliques):
        clique_color = colormap(idx / len(cliques))

        # Draw edges within cliques
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                if G.has_edge(clique[i], clique[j]):
                    ax.plot([pos[clique[i]][0], pos[clique[j]][0]],
                            [pos[clique[i]][1], pos[clique[j]][1]],
                            color=clique_color, linewidth=2, alpha=1)

        # Draw edges from non-clique nodes to clique's centroid
        centroid = clique_centroids[idx]
        for node in non_clique_nodes:
            for clique_member in clique:
                if G.has_edge(node, clique_member):
                    ax.plot([pos[node][0], centroid[0]], [pos[node][1], centroid[1]],
                            color='grey', linestyle='--', linewidth=1, alpha=0.2)
                    break  # Assume only one edge per non-clique node to the clique for simplicity

    # Draw the rest of the graph
    nx.draw(G, pos, ax=ax, node_color='black', edge_color='gray', node_size=20, alpha=1)

    # Movement and force vectors as before...


    # Draw movement lines
    for i in pos.keys():
        if i in old_pos:
            ax.plot([old_pos[i][0], pos[i][0]], [old_pos[i][1], pos[i][1]], color='grey', linestyle='-', linewidth=1, alpha=0.5)

    for i, vectors in force_vectors['repulsive'].items():
        for j, vector in vectors:
            ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.002, alpha=0.5)

    for (i, j), vector in force_vectors['attractive'].items():
        ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.002, alpha=0.5)

