import networkx as nx
import matplotlib.pyplot as plt

def load_graph():
    # Load the Zachary's Karate Club Graph
    return nx.karate_club_graph()

def find_minimum_cut(G):
    # Find the minimum cut using the Stoer-Wagner algorithm
    cut_value, (set1, set2) = nx.stoer_wagner(G)
    return cut_value, set1, set2

def plot_graph(G, set1, set2):
    # Color nodes based on their set
    color_map = []
    for node in G:
        if node in set1:
            color_map.append('blue')
        else:
            color_map.append('red')

    # Draw the graph
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, node_color=color_map, with_labels=True, node_size=400)
    plt.show()

def main():
    G = load_graph()
    cut_value, set1, set2 = find_minimum_cut(G)
    print(f'Minimum cut value: {cut_value}')
    print(f'Nodes in set 1: {set1}')
    print(f'Nodes in set 2: {set2}')
    plot_graph(G, set1, set2)

if __name__ == '__main__':
    main()
