from graph_initializer import create_graph

# Import functionalities from the network package
from network import apply_forces, update_positions, initialize_positions, print_node_clique_membership_from_selected, plot_graph, find_max_cliques, simulate

# Example to initialize and apply forces (you'll need to add your logic for iterating and cooling)
G = create_graph() # or your custom graph
pos = initialize_positions(G)
displacement, force_vectors = apply_forces(G, pos)
pos = update_positions(pos, displacement)

# Identify and visualize cliques
selected_cliques = find_max_cliques(G)
print_node_clique_membership_from_selected(G, selected_cliques)
simulate(G, iterations=100, plot_every_n_steps=5)
