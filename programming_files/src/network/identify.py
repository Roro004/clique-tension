import networkx as nx
import matplotlib.pyplot as plt
import itertools

# def find_max_cliques(G):
#     pos = nx.spring_layout(G)
#     cliques = list(nx.find_cliques(G))
#     cliques.sort(key=len, reverse=True)
#     selected_cliques = []
#     selected_nodes = set()
#     for clique in cliques:
#         if not any(node in selected_nodes for node in clique):
#             selected_cliques.append(clique)
#             selected_nodes.update(clique)


#     return selected_cliques


def find_max_cliques(G):
    # This line can be omitted if the layout is not necessary for the algorithm
    pos = nx.spring_layout(G)
    cliques = list(nx.find_cliques(G))
    cliques.sort(key=len, reverse=True)
    expanded_cliques = []

    for original_clique in cliques:
        expanded_clique = original_clique.copy()

        # Check each node outside the clique to see if it should be added
        external_nodes = set(G.nodes()) - set(expanded_clique)
        for node in external_nodes:
            connections_to_clique = sum(1 for neighbor in G.neighbors(node) if neighbor in expanded_clique)
            if connections_to_clique > len(expanded_clique) / 2:
                expanded_clique.append(node)

        # It's important to sort or otherwise handle the expanded_clique here
        # if the order or specific arrangement of nodes within it matters later
        expanded_cliques.append(expanded_clique)

    return expanded_cliques



# def find_max_cliques(G):
#     # Omit layout calculation if not needed for the algorithm
#     cliques = list(nx.find_cliques(G))
#     cliques.sort(key=len, reverse=True)  # Prioritize larger cliques
#     expanded_cliques = []

#     for original_clique in cliques:
#         expanded_clique = original_clique.copy()

#         # Check each node not currently in the clique
#         external_nodes = set(G.nodes()) - set(expanded_clique)
#         for node in external_nodes:
#             # Convert neighbors iterator to list to use len()
#             neighbors_of_node = list(G.neighbors(node))
#             connections_to_clique = sum(1 for neighbor in neighbors_of_node if neighbor in expanded_clique)

#             # If more than 50% of 'node's neighbors are in the clique, add 'node' to the clique
#             if connections_to_clique > len(neighbors_of_node) / 3:
#                 expanded_clique.append(node)

#         # Ensure the expanded clique is ordered or arranged as needed before appending
#         expanded_cliques.append(expanded_clique)

#     return expanded_cliques


# def find_max_cliques(G):
#     cliques = list(nx.find_cliques(G))
#     cliques.sort(key=len, reverse=True)  # Prioritize larger cliques
#     expanded_cliques = []

#     for original_clique in cliques:
#         expanded_clique = original_clique.copy()

#         # Check each node not currently in the clique
#         external_nodes = set(G.nodes()) - set(expanded_clique)
#         for node in external_nodes:
#             # Convert neighbors iterator to list to use len()
#             neighbors_of_node = list(G.neighbors(node))
#             connections_to_clique = sum(1 for neighbor in neighbors_of_node if neighbor in expanded_clique)

#             # If more than 2/3 of 'node's neighbors are in the clique, add 'node' to the clique
#             if connections_to_clique > (3/5) * len(neighbors_of_node):
#                 expanded_clique.append(node)

#         expanded_cliques.append(expanded_clique)

#     return expanded_cliques



def map_nodes_to_cliques(G):
    """
    Map each node in the graph to the index of the clique it belongs to.

    Parameters:
    - G (networkx.Graph): The graph containing nodes and edges.

    Returns:
    - dict: A dictionary where keys are node identifiers and values are the indices of the cliques to which the nodes belong.
    """
    cliques = find_max_cliques(G)
    node_to_clique = {}
    for index, clique in enumerate(cliques):
        for node in clique:
            node_to_clique[node] = index
    return node_to_clique


def print_node_clique_membership_from_selected(G, selected_cliques):
    node_cliques = {node: [] for node in G.nodes()}
    for clique_id, clique in enumerate(selected_cliques, start=1):
        for node in clique:
            node_cliques[node].append(clique_id)

    for node, cliques in node_cliques.items():
        print(f"Node {node} is in selected cliques: {cliques}")
