# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:59:12 2020

@authors: Jeremiah Neuneker, Julia Ramirez, Warda Qadeer, Noah V.
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def show_weighted_graph(G):
    pos = nx.planar_layout(G)
    nx.draw(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G,
                                 pos,
                                 edge_labels = labels)
    plt.show()
    

def draw_subtree(G, T):
    pos = nx.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G,
                                pos,
                                edge_labels = labels,)
    nx.draw_networkx_edges(G, pos,
                           edgelist = T.edges(),
                           width = 9, alpha = 0.5,
                           edge_color = 'r',)
    nx.draw_networkx_nodes(G,
                           pos,
                           nodelist = T.nodes(),
                           node_color = 'r',
                           node_size = 500,
                           alpha = 0.8)
    plt.show()