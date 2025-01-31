"""
Author: Alpha Team Group Project
Date: March 2023
Purpose: Stochastic approximation algorithms for estimating graph properties Leveraging sampling techniques to improve computational efficiency
"""

# ------------------------------------------------------------------------------

import networkx as nx
# External import
import numpy as np
import pandas as pd
from tqdm import tqdm


# ------------------------------- UTILS FUNCTIONS -------------------------------------

def get_random_sample(nodes):
    """
    :Function: Get random sample of 2 nodes from nodes
    :param nodes: list of nodes
    :type nodes: list
    :return: random sample of 2 nodes from nodes
    :rtype: list
    """
    return np.random.choice(nodes, size=2, replace=False)


# -------------------------------------------------------------------------------------

def get_random_node(nodes):
    """
    :Function: Get random node from nodes
    :param nodes: list of nodes
    :type nodes: list
    :return: random node from nodes
    :rtype: list
    """
    return np.random.choice(nodes, size=1, replace=False)


# -------------------------------------- FUNCTIONS -------------------------------------


def estimate_shortest_path_length(networkGraphs, iterations=10_000):
    """
    :Function: Estimate shortest path length between over a iterations number of samples
    :param networkGraphs: NetworkGraphs object
    :type networkGraphs: src.NetworkGraphs.NetworkGraphs
    :param iterations: Number of samples
    :type iterations: int
    :return: DataFrame of shortest path lengths
    :rtype: pandas.core.frame.DataFrame
    """
    G = networkGraphs.Graph
    nodes = list(G.nodes())
    lengths = []

    for _ in tqdm(range(iterations)):
        node1, node2 = get_random_sample(nodes)
        try:
            length = nx.shortest_path_length(G, node1, node2)
            lengths.append(length)
        except nx.NetworkXNoPath:
            pass

    df = pd.DataFrame({
        'Sample': range(len(lengths)),
        'Shortest Path Length': lengths,
    })

    return df


# -------------------------------------------------------------------------------------


def estimate_clustering_coefficient(networkGraphs, iterations=10_000):
    """
    :Function: Estimate clustering coefficient over a iterations number of samples
    :param networkGraphs: NetworkGraphs object
    :type networkGraphs: src.NetworkGraphs.NetworkGraphs
    :param iterations: Number of samples
    :type iterations: int
    :return: DataFrame of clustering coefficients
    :rtype: pandas.core.frame.DataFrame
    """
    G = networkGraphs.Graph
    nodes = list(G.nodes())
    coefficients = []

    for _ in tqdm(range(iterations)):
        node = get_random_node(nodes)[0]
        coefficient = nx.clustering(G, node)
        coefficients.append(coefficient)

    df = pd.DataFrame({
        'Sample': range(len(coefficients)),
        'Clustering Coefficient': coefficients,
    })

    return df
