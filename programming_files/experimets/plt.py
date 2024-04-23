import networkx as nx
import matplotlib.pyplot as plt

# Create a simple graph that illustrates mutual, asymmetric, and null relationships
G = nx.DiGraph()  # Directed graph to illustrate asymmetric and mutual relationships

# Adding nodes
G.add_nodes_from(range(1, 6))

# Adding edges
# Mutual choices (M): 1 <-> 2
G.add_edge(1, 2)
G.add_edge(2, 1)

# Asymmetric choices (A): 3 -> 4
G.add_edge(3, 4)

# Null choices (N) is implicit, no direct edge between some nodes like 4 and 1

# Set positions
pos = {1: (0, 1), 2: (1, 1), 3: (2, 0), 4: (3, 1), 5: (4, 0)}

# Draw the graph
plt.figure(figsize=(8, 5))
nx.draw(G, pos, with_labels=True, node_size=2500, node_color='skyblue', font_size=16, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(1, 2): 'M', (2, 1): 'M', (3, 4): 'A'}, font_color='red')

# Title and axis
plt.title('Graph Illustrating Mutual, Asymmetric, and Null Choices')
plt.axis('off')  # Turn off the axis for a cleaner look
plt.show()
