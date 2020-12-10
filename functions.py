# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:55:28 2020

@authors: Jeremiah Neuneker, Julia Ramirez, Warda Qadeer, Noah V.
"""

import networkx as nx

# Function to return set of vertices
def V(graph):
    return set(graph.nodes())

# Function to return set of edges
def E(graph):
    return set(graph.edges())

# Function to intialize the tree
# v is the starting vertex/node
def prims_initialize(graph , v):
    if v not in V(graph):
        return 'Error vertex not found'
    T = nx.Graph()
    T.add_node(v)
    return T

# Function to check if graph is spanning (i.e. have we spanned across all vertices/nodes)
def is_spanning(graph, subgraph):
    return V(graph) ==  V(subgraph)

# Function to return the weight of the edge
# e is the nodes on either side of the edge
def cost(G, e):
    return G[e[0]][e[1]]['weight']

# Function to return the list of possible edges remaining
def possible_edges(G, T):
    return [e for e in list(G.edges(V(T))) 
             if e[0] not in V(T)
             or e[1] not in V(T)]

# Function to return the edge with the lowest cost/weight
def min_cost_edge(G, T):
    edge_list = possible_edges(G, T)
    edge_list.sort(key = lambda e : cost(G, e))
    return edge_list[0]