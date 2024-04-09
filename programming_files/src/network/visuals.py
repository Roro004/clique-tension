import matplotlib.pyplot as plt
import networkx as nx
from network.identify import find_max_cliques
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Circle

def plot_graph(G, pos, old_pos, force_vectors, cliques, ax):
    ax.clear()

    # Calculate centroids of cliques
    clique_centroids = {}
    for idx, clique in enumerate(cliques):
        x_coords = [pos[node][0] for node in clique]
        y_coords = [pos[node][1] for node in clique]
        centroid = (sum(x_coords) / len(x_coords), sum(y_coords) / len(y_coords))
        clique_centroids[idx] = centroid
        # Optional: Draw a red circle at each centroid for visual reference
        circle = Circle(centroid, .5, color='red', fill=True, alpha=0.6)
        ax.add_patch(circle)

    # Prepare a mapping from node to its clique index and centroid
    node_to_clique_info = {}
    for idx, clique in enumerate(cliques):
        for node in clique:
            node_to_clique_info[node] = (idx, clique_centroids[idx])

    # Draw edges based on the type
    colormap = plt.cm.get_cmap('Pastel1', len(cliques))
    for node1, node2 in G.edges():
        # Determine the type of edge
        if node1 in node_to_clique_info and node2 in node_to_clique_info:
            clique1, centroid1 = node_to_clique_info[node1]
            clique2, centroid2 = node_to_clique_info[node2]

            if clique1 == clique2:  # Same clique
                ax.plot([pos[node1][0], pos[node2][0]], [pos[node1][1], pos[node2][1]],
                        color=colormap(clique1), linewidth=2, alpha=1)
            else:  # Different cliques
                ax.plot([centroid1[0], centroid2[0]], [centroid1[1], centroid2[1]],
                        color='grey', linestyle='--', linewidth=1, alpha=0.6)
        else:
            # Edge from a node to a clique centroid
            if node1 in node_to_clique_info:
                centroid = node_to_clique_info[node1][1]
                ax.plot([pos[node2][0], centroid[0]], [pos[node2][1], centroid[1]],
                        color='grey', linewidth=1, alpha=0.3)
            if node2 in node_to_clique_info:
                centroid = node_to_clique_info[node2][1]
                ax.plot([pos[node1][0], centroid[0]], [pos[node1][1], centroid[1]],
                        color='grey', linewidth=1, alpha=0.3)

    # Draw nodes
    nx.draw(G, pos, ax=ax, node_color='black', edge_color='gray', node_size=20, alpha=1)
    # Add move
    # Movement and force vectors as before...



# def plot_graph(G, pos, old_pos, force_vectors, cliques, ax):
#     ax.clear()

#     # Create a dictionary to map each node to its clique's centroid
#     node_to_centroid = {}
#     for idx, clique in enumerate(cliques):
#         # Calculate centroid for this clique
#         x_coords = [pos[node][0] for node in clique]
#         y_coords = [pos[node][1] for node in clique]
#         centroid = (sum(x_coords) / len(clique), sum(y_coords) / len(clique))

#         # Draw red circle at centroid
#         circle = Circle(centroid, 0.5, color='red', fill=True, alpha=0.6)
#         ax.add_patch(circle)

#         # Map each node in the clique to this centroid
#         for node in clique:
#             node_to_centroid[node] = centroid

#     # Draw edges
#     for node1, node2 in G.edges():
#         # Both nodes in cliques and mapped to the same centroid (within same clique)
#         if node1 in node_to_centroid and node2 in node_to_centroid and node_to_centroid[node1] == node_to_centroid[node2]:
#             ax.plot([pos[node1][0], pos[node2][0]],
#                     [pos[node1][1], pos[node2][1]],
#                     color='blue', linewidth=2, alpha=0.6)
#         else:
#             # At least one node not in any clique or in different cliques
#             centroid1 = node_to_centroid.get(node1, pos[node1])
#             centroid2 = node_to_centroid.get(node2, pos[node2])
#             ax.plot([centroid1[0], centroid2[0]],
#                     [centroid1[1], centroid2[1]],
#                     color='grey', linestyle='--', linewidth=1, alpha=0.6)

#     # Draw nodes
#     nx.draw(G, pos, ax=ax, node_color='black', edge_color='gray', node_size=20, alpha=1)



# identifies clique edges and colours correctily
# def plot_graph(G, pos, old_pos, force_vectors, cliques, ax):
#     ax.clear()

#     all_clique_nodes = set(node for clique in cliques for node in clique)
#     all_nodes = set(G.nodes())
#     non_clique_nodes = all_nodes - all_clique_nodes

#     clique_centroids = {}
#     for idx, clique in enumerate(cliques):
#         x_coords = [pos[node][0] for node in clique]
#         y_coords = [pos[node][1] for node in clique]
#         centroid = (sum(x_coords) / len(clique), sum(y_coords) / len(clique))
#         clique_centroids[idx] = centroid

#         # Draw a red circle at the centroid
#         circle = Circle(centroid, 0.05, color='red', fill=True, alpha=0.6)  # Adjust size and alpha as needed
#         ax.add_patch(circle)

#     colormap = plt.cm.get_cmap('Pastel2_r', len(cliques))

#     for idx, clique in enumerate(cliques):
#         clique_color = colormap(idx / len(cliques))

#         for i in range(len(clique)):
#             for j in range(i + 1, len(clique)):
#                 if G.has_edge(clique[i], clique[j]):
#                     ax.plot([pos[clique[i]][0], pos[clique[j]][0]],
#                             [pos[clique[i]][1], pos[clique[j]][1]],
#                             color=clique_color, linewidth=2, alpha=0.6)

#         centroid = clique_centroids[idx]
#         for node in non_clique_nodes:
#             for clique_member in clique:
#                 if G.has_edge(node, clique_member):
#                     ax.plot([pos[node][0], centroid[0]], [pos[node][1], centroid[1]],
#                             color='grey', linestyle='--', linewidth=1, alpha=0.6)
#                     break

#     nx.draw(G, pos, ax=ax, node_color='black', edge_color='gray', node_size=20, alpha=1)

    # Add movement and force vectors as previously defined...





    # Draw movement lines
    for i in pos.keys():
        if i in old_pos:
            ax.plot([old_pos[i][0], pos[i][0]], [old_pos[i][1], pos[i][1]], color='grey', linestyle='-', linewidth=1, alpha=0.5)

    for i, vectors in force_vectors['repulsive'].items():
        for j, vector in vectors:
            ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.002, alpha=0.5)

    for (i, j), vector in force_vectors['attractive'].items():
        ax.quiver(pos[i][0], pos[i][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.002, alpha=0.5)

