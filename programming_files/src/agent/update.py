from agent.score import structural_balance_score
import random


def update_graph(G, N=1000, n_iter=100):
    n = G.number_of_nodes()
    for _ in range(n_iter):
        total_SB_change = 0
        for _ in range(N):
            # Pick a node i at random.
            i = random.randint(0, n-1)
            neighbors_i = list(G.neighbors(i))

            # For each neighbor, evaluate the impact of flipping each edge on all relevant triads.
            for j in neighbors_i:
                # Find other neighbors to form triads.
                for k in [x for x in neighbors_i if x != j]:
                    # Only proceed if j and k are also connected, forming a triad.
                    if G.has_edge(j, k) or G.has_edge(k, j):
                        # Calculate the current structural balance score for the triad.
                        current_SB = structural_balance_score(G, i, j, k)

                        # Flip the edge between i and j, simulate its impact.
                        G[i][j]['weight'] *= -1
                        flipped_SB = structural_balance_score(G, i, j, k)
                        G[i][j]['weight'] *= -1  # Flip back after simulation

                        # If flipping improves the structural balance, apply the flip.
                        if flipped_SB > current_SB:
                            G[i][j]['weight'] *= -1  # Actually flip the sign
                            total_SB_change += abs(flipped_SB - current_SB)

                        # Similar logic for the edge between i and k, if needed.

        # Exit if the total SB change is 0, indicating no improvement can be made.
        if total_SB_change == 0:
            break

    return G
