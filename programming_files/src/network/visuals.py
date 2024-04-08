import matplotlib.pyplot as plt
import networkx as nx
from network.identify import find_max_cliques
def plot_graph(G, pos, old_pos, force_vectors, cliques, ax):
    ax.clear()

    # Get a colormap from matplotlib, dynamically adjusting to the number of cliques
    colormap = plt.cm.get_cmap('Pastel2_r', len(cliques))

    # Highlight edges within each clique using colors from the colormap
    for idx, clique in enumerate(cliques):
        clique_color = colormap(idx / len(cliques))  # Normalize idx to the range [0, 1]

        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                if G.has_edge(clique[i], clique[j]):
                    ax.plot([pos[clique[i]][0], pos[clique[j]][0]],
                            [pos[clique[i]][1], pos[clique[j]][1]],
                            color=clique_color, linewidth=2, alpha=0.6)

    # Draw the rest of the graph, possibly adjusting parameters for visibility
    nx.draw(G, pos, ax=ax, node_color='black', edge_color='gray', node_size=20, alpha=1)



    # Draw movement lines
    for i in pos.keys():
        if i in old_pos:
            ax.plot([old_pos[i][0], pos[i][0]], [old_pos[i][1], pos[i][1]], color='grey', linestyle='-', linewidth=1, alpha=0.5)

    for i, vectors in force_vectors['repulsive'].items():
        for j, vector in vectors:
            ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.002, alpha=0.5)

    for (i, j), vector in force_vectors['attractive'].items():
        ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.002, alpha=0.5)

