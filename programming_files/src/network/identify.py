import networkx as nx
import matplotlib.pyplot as plt
import itertools

def find_max_cliques(G):
    pos = nx.spring_layout(G)
    cliques = list(nx.find_cliques(G))
    cliques.sort(key=len, reverse=True)
    selected_cliques = []
    selected_nodes = set()
    for clique in cliques:
        if not any(node in selected_nodes for node in clique):
            selected_cliques.append(clique)
            selected_nodes.update(clique)


    return selected_cliques

def print_node_clique_membership_from_selected(G, selected_cliques):
    node_cliques = {node: [] for node in G.nodes()}
    for clique_id, clique in enumerate(selected_cliques, start=1):
        for node in clique:
            node_cliques[node].append(clique_id)

    for node, cliques in node_cliques.items():
        print(f"Node {node} is in selected cliques: {cliques}")
