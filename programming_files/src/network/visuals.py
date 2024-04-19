import matplotlib.pyplot as plt
import networkx as nx
from graph_initializer import create_graph ,positive_edges, negative_edges
from network.identify import find_max_cliques, map_nodes_to_cliques

def plot_graph(G, pos, old_pos, force_vectors, ax):
    ax.clear()
    # nx.draw(G, pos, ax=ax, node_color='black', node_size=50)


    # Drawing nodes
    # nx.draw_networkx_nodes(G, pos, node_size=50)

    cliques = find_max_cliques(G)  # Retrieve the list of cliques
    node_to_clique = map_nodes_to_cliques(G)  # This is the mapping from nodes to clique indices

    # Initialize the colormap
    colormap = plt.cm.get_cmap('Pastel2_r', len(cliques))

    # Create a color map for nodes based on their clique index
    node_color = {node: colormap(node_to_clique[node] / len(cliques)) for node in G.nodes()}

    # Drawing nodes with colors mapped by cliques
    nx.draw(G, pos, ax=ax, node_color=[node_color.get(node, 'black') for node in G.nodes()],
            node_size=50, with_labels=False)


    # Drawing edges
    nx.draw_networkx_edges(G, pos, edgelist=positive_edges(G), width=2, alpha=0.5, edge_color='green')
    nx.draw_networkx_edges(G, pos, edgelist=negative_edges(G), width=2, alpha=0.5, edge_color='red')
    # Draw movement lines
    for i in pos.keys():
        if i in old_pos:
            ax.plot([old_pos[i][0], pos[i][0]], [old_pos[i][1], pos[i][1]], color='grey', linestyle='-', linewidth=1, alpha=0.5)

    for i, vectors in force_vectors['repulsive'].items():
        for j, vector in vectors:
            ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.002, alpha=0.5)

    for (i, j), vector in force_vectors['attractive'].items():
        ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.002, alpha=0.5)
