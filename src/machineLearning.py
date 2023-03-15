"""
Author: Alpha Team Group Project
Date: March 2023
Purpose: Machine Learning for the NetworkX graphs
"""

import networkx.algorithms.community as nx_comm
import pandas as pd
from distinctipy import distinctipy


def short_path_distance(networkx_, from_, to_):
    # return dataframe
    return 0


def get_cold_spot(networkx_):
    # return dataframe
    return 0


def get_hot_spot(networkx_):
    # return dataframe
    return 0


def create_comm_colors(communities):
    colors = distinctipy.get_colors(len(communities))
    colors = [tuple([i * 255 for i in c]) for c in colors]
    # convert rgb tuple to hex
    colors = [f'#{int(c[0]):02x}{int(c[1]):02x}{int(c[2]):02x}' for c in colors]

    return colors


def create_comm_dataframe(communities, colors):
    df = pd.DataFrame()
    for idx, community in enumerate(communities):
        color = colors.pop()
        for node in community:
            # concat node, color, cluster_id into dataframe
            df = pd.concat([df, pd.DataFrame({'Node': node,
                                              'Color': color,
                                              'Cluster_id': idx
                                              }, index=[0])], ignore_index=True)
    return df


def louvain_clustering(networkGraphs):
    """

    :param networkGraphs:
    :return:
    """
    # get the communities on the graph
    communities = list(nx_comm.louvain_communities(networkGraphs.Graph))
    colors = create_comm_colors(communities)
    df = create_comm_dataframe(communities, colors)

    return df


def greedy_modularity_clustering(networkGraphs):
    """
    Detect communities based on modularity.
    :param networkGraphs:
    :return:
    """
    communities = list(nx_comm.greedy_modularity_communities(networkGraphs.Graph))
    colors = create_comm_colors(communities)
    # create empty dataframe
    df = create_comm_dataframe(communities, colors)
    return df


def label_propagation_clustering(networkGraphs):
    communities = list(nx_comm.label_propagation_communities(networkGraphs.Graph))
    colors = create_comm_colors(communities)
    df = create_comm_dataframe(communities, colors)
    return df


def asyn_lpa_clustering(networkGraphs):
    communities = list(nx_comm.asyn_lpa_communities(networkGraphs.Graph))
    colors = create_comm_colors(communities)
    df = create_comm_dataframe(communities, colors)
    return df


def girvan_newman_clustering(networkGraphs):
    communities = list(nx_comm.girvan_newman(networkGraphs.Graph))
    colors = create_comm_colors(communities)
    df = create_comm_dataframe(communities, colors)
    return df


def edge_betweenness_clustering(networkGraphs):
    communities = list(nx_comm.centrality.girvan_newman(networkGraphs.Graph))
    colors = create_comm_colors(communities)
    df = create_comm_dataframe(communities, colors)
    return df


def k_clique_clustering(networkGraphs):
    communities = list(nx_comm.k_clique_communities(networkGraphs.Graph, 3))
    colors = create_comm_colors(communities)
    df = create_comm_dataframe(communities, colors)
    return df


def get_communities(networkGraphs, method):
    if method not in ['louvain', 'greedy_modularity', 'label_propagation', 'asyn_lpa', 'girvan_newman',
                      'edge_betweenness', 'k_clique']:
        print("Invalid cluster type")
        return

    if method == 'louvain':
        return louvain_clustering(networkGraphs)
    elif method == 'greedy_modularity':
        return greedy_modularity_clustering(networkGraphs)
    elif method == 'label_propagation':
        return label_propagation_clustering(networkGraphs)
    elif method == 'asyn_lpa':
        return asyn_lpa_clustering(networkGraphs)
    elif method == 'girvan_newman':
        return girvan_newman_clustering(networkGraphs)
    elif method == 'edge_betweenness':
        return edge_betweenness_clustering(networkGraphs)
    elif method == 'k_clique':
        return k_clique_clustering(networkGraphs)
    else:
        return None
