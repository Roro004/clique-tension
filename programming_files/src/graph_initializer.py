import networkx as nx

def create_graph():
    # 1: Karate
    G = nx.karate_club_graph()
    G = nx.powerlaw_cluster_graph(40,4,.06)
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
