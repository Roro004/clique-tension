import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

# Seed for reproducibility
random.seed(42)

# Initialize a complete graph with 3 vertices
G = nx.complete_graph(3)

# Assign random signs to each edge with a probability of 0.5
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = 1
    G.edges[u, v]['accum_weight'] = G.edges[u, v]['weight']

# Position of the vertices, initialized with float values
pos = {0: np.array([0.0, 0.0]), 1: np.array([1.0, 0.0]), 2: np.array([0.5, np.sin(np.pi/3)])}

def update_positions():
    # Calculate the center of mass based on signed weights
    center = np.zeros(2)
    total_weight = 0
    for i in pos:
        weight_contrib = sum(G.edges[i, j]['accum_weight'] for j in G.neighbors(i))
        center += pos[i] * weight_contrib
        total_weight += weight_contrib
    if total_weight != 0:
        center /= total_weight

    # Move vertices slightly towards or away from the center based on total signed weight
    for i in pos:
        direction = center - pos[i]
        if np.linalg.norm(direction) != 0:
            move = direction / np.linalg.norm(direction) * 0.05 * np.sign(sum(G.edges[i, j]['accum_weight'] for j in G.neighbors(i)))
            pos[i] += move

def plot_graph(step):
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos=pos, with_labels=True, node_color='skyblue', node_size=700,
            edge_color=['green' if G[u][v]['accum_weight'] > 0 else 'red' for u, v in G.edges()],
            width=[abs(G[u][v]['accum_weight']) for u, v in G.edges()])
    plt.title(f"Step {step}")
    plt.show()

# Simulation parameters
num_steps = 10

# Run the simulation
for step in range(num_steps):
    # Increment weights and update positions
    for (u, v) in G.edges():
        G.edges[u, v]['accum_weight'] += G.edges[u, v]['weight']

    update_positions()
    plot_graph(step + 1)
