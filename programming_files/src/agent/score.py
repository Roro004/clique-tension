def structural_balance_score(G, i, j, k):
    """Calculate the structural balance score for a triad."""
    w_ij = G[i][j]['weight']
    w_ik = G[i][k]['weight']
    w_jk = G[j].get(k, {}).get('weight', 0)
    w_kj = G[k].get(j, {}).get('weight', 0)
    return w_ij * w_ik * (w_jk + w_kj)
