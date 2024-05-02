import networkx as nx
import random

p_positive = 0.5
n_nodes=3
density = 0.5



def create_graph():

    #{0,1,2}
    # {0,1}-> +1, {1,0} -> 0, {1,2}-> +1. {2,1}->+1,


    # 1: Karate

    p_positive = 1
    G = nx.complete_graph(n_nodes)
    G = nx.DiGraph(G)

    # for (u, v) in G.edges():
    #     G[u][v]['weight'] = 1 if random.random() < p_positive else -1

    # all_possible_edges = [(i, j) for i in range(n_nodes) for j in range(n_nodes) if i != j]

    # # Calculate the number of edges based on density
    # max_edges = n_nodes * (n_nodes - 1)
    # non_zero_edges_count = int(max_edges * density)
    # zero_edges_count = max_edges - non_zero_edges_count

    # # Randomly shuffle and assign zero weights to the remaining edges
    # random.shuffle(all_possible_edges)
    # zero_edges = all_possible_edges[non_zero_edges_count:]
    # non_zero_edges = all_possible_edges[:non_zero_edges_count]

    # # Assign zero weights
    # for u, v in zero_edges:
    #     G.add_edge(u, v, weight=0)

    # # Determine counts for positive and negative weights within non-zero edges
    # positive_edges_count = int(non_zero_edges_count * p_positive)
    # negative_edges_count = non_zero_edges_count - positive_edges_count

    # # Assign weights to the non-zero edges
    # positive_edges = non_zero_edges[:positive_edges_count]
    # negative_edges = non_zero_edges[positive_edges_count:]

    # for u, v in positive_edges:
    #     G.add_edge(u, v, weight=1)
    # for u, v in negative_edges:
    #     G.add_edge(u, v, weight=-1)

    # return G








    G[0][1]['weight'] = 1
    G[1][0]['weight'] = -1

    G[1][2]['weight'] = -1
    G[2][1]['weight'] = 1

    G[2][0]['weight'] = -1
    G[0][2]['weight'] = -1

    return G

    # G = nx.Graph()
    # # 2: 89 nodes
    # file_path = 'programming_files/src/data/email_eu_3_89'
    # # 3: 142 nodes
    # file_path = 'programming_files/src/data/email_eu_4_142'
    # # 4: 162 nodes
    # file_path = 'programming_files/src/data/email_eu_4_162.txt'
    # # 5: 309 nodes
    # file_path = 'programming_files/src/data/email_eu_1_309'
    # # 6: 986 nodes
    # file_path = 'programming_files/src/data/986'

    # Read the edges from the file and add them to the graph
    # with open(file_path, 'r') as file:
    #     for line in file:
    #         node1, node2, _ = line.strip().split()
    #         G.add_edge(int(node1), int(node2))


# file_path = 'programming_files/src/data/edges'  # Adjust the path if your file is located elsewhere

# # Read the edges from the file and add them to the graph
# with open(file_path, 'r') as file:
#     for line in file:
#         node1, node2 = line.strip().split()
#         G.add_edge(int(node1), int(node2))


# file_path = 'programming_files/src/data/congress.edgelist'  # Adjust the path if your file is located elsewhere

# # Read the edges from the file and add them to the graph
# with open(file_path, 'r') as file:
#     for line in file:
#         parts = line.strip().split()  # Splitting the line into parts
#         if len(parts) >= 2:  # Making sure there are at least two elements (for the nodes)
#             node1, node2 = parts[:2]  # Taking only the first two elements
#             G.add_edge(int(node1), int(node2))  # Adding the edge to the graph


# file_path = 'programming_files/src/data/lastfm_asia_edges'
# with open(file_path, 'r') as file:
#     for line in file:
#         node1, node2 = line.strip().split(',')
#         G.add_edge(int(node1), int(node2))


    print(G)
    return G
def positive_edges(G):
    return [(u, v) for u, v, d in G.edges(data=True) if d.get('weight', 0) > 0]

def negative_edges(G):
    return [(u, v) for u, v, d in G.edges(data=True) if d.get('weight', 0) < 0]
