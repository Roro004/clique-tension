import networkx as nx
import matplotlib.pyplot as plt
import itertools
import numpy as np

def draw_network_with_colored_cliques_and_edges(G):
    # Position nodes using the spring layout
    pos = nx.spring_layout(G)

    # Detect all maximal cliques in the graph
    cliques = list(nx.find_cliques(G))

    # Sort cliques by size
    cliques.sort(key=len, reverse=True)

    # Initialize a color map for nodes and edges
    node_color = {}
    edge_color = {}
    colors = itertools.cycle(plt.cm.tab20.colors)  # Cycle through a colormap

    # Select the largest non-overlapping cliques
    selected_cliques = []
    selected_nodes = set()
    for clique in cliques:
        if not any(node in selected_nodes for node in clique):
            selected_cliques.append(clique)
            selected_nodes.update(clique)
            clique_color = next(colors)  # Get a color for the clique
            for node in clique:
                node_color[node] = clique_color  # Assign color to each node in the clique
            for u, v in itertools.combinations(clique, 2):
                if G.has_edge(u, v) or G.has_edge(v, u):
                    edge_color[(u, v)] = clique_color
                    edge_color[(v, u)] = clique_color  # For undirected graphs

    # Assign black color to non-clique nodes
    for node in G.nodes():
        if node not in selected_nodes:
            node_color[node] = 'black'

    # Assign gray color to non-clique edges
    for u, v in G.edges():
        if (u, v) not in edge_color and (v, u) not in edge_color:
            edge_color[(u, v)] = 'gray'

    # Create edge color list in the same order as G.edges()
    edge_color_list = [edge_color[edge] if edge in edge_color else 'gray' for edge in G.edges()]

    # Draw the network
    nx.draw(G, pos, node_color=[node_color[node] for node in G.nodes()], edge_color=edge_color_list)

    plt.show()
    return selected_cliques

def print_node_clique_membership_from_selected(G, selected_cliques):
    # Map each node to the cliques it belongs to, based on selected cliques
    node_cliques = {node: [] for node in G.nodes()}
    for clique_id, clique in enumerate(selected_cliques, start=1):
        for node in clique:
            node_cliques[node].append(clique_id)

    # Print the clique memberships
    for node, cliques in node_cliques.items():
        print(f"Node {node} is in selected cliques: {cliques}")

# Example usage
G = nx.Graph()

file_path = 'Embedding/email_eu_3_89'  # Adjust the path if your file is located elsewhere

# Read the edges from the file and add them to the graph
with open(file_path, 'r') as file:
    for line in file:
        node1, node2, _ = line.strip().split()
        G.add_edge(int(node1), int(node2))

selected_cliques = draw_network_with_colored_cliques_and_edges(G)
print_node_clique_membership_from_selected(G, selected_cliques)
