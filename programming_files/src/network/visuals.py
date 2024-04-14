import matplotlib.pyplot as plt
import networkx as nx
from graph_initializer import create_graph ,positive_edges, negative_edges

def plot_graph(G, pos, old_pos, force_vectors, ax):
    ax.clear()
    nx.draw(G, pos, ax=ax, node_color='black', node_size=50)


    # Drawing nodes
    nx.draw_networkx_nodes(G, pos, node_size=50)

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

