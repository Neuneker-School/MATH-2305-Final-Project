# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:55:28 2020

@authors: Jeremiah Neuneker, Julia Ramirez, Warda Qadeer, Noah V.
"""

import networkx as nx

def V(graph):
    """Takes in a number of vertices.
    
    Parameters   
    ----------
    
    Returns    
    -------    
    A graph with set number of vertices.
    """
    return set(graph.nodes())

def E(graph):
     """Takes in a number of edges.
    
    Parameters   
    ----------
    
    Returns    
    -------    
    A graph with set number of edges.
    """
    return set(graph.edges())

def prims_initialize(graph , v):
     """Function to intialize the tree
    
    Parameters   
    ----------
    graph : NetworkX graph 
    
    v : starting vertex/node
    
    Returns    
    -------  
    Error if vertix is not found, otherwise graph.
    """
    
    if v not in V(graph):
        return 'Error vertex not found'
    T = nx.Graph()
    T.add_node(v)
    return T

def is_spanning(graph, subgraph):
    """Checks to see if graph is spanning.
    
    Parameters   
    ----------
    Graph
    Subgraph
    
    Returns    
    -------    
    A graph containing all spanning vertices/nodes
    """
    return V(graph) ==  V(subgraph)

def cost(G, e):
    """Returns the weight of the edges of G.
    
    Parameters
    ----------
    G: NetworkX graph
    
    e : the nodes on either side of the edge.
    
    Returns
    -------
    Weight of the edges of G.
    """
    return G[e[0]][e[1]]['weight']

def possible_edges(G, T):
    """Returns the list of possible edges remaining.
    
    Parameters
    ----------
    G : NetworkX graph
    
    T : Prim's Algorithm
    
    Returns
    -------
    List of possible edges remaining.
    """
    return [e for e in list(G.edges(V(T))) 
             if e[0] not in V(T)
             or e[1] not in V(T)]

def min_cost_edge(G, T):
    """Returns the edge with the lowest cost/weight. 
    
    Parameters
    ----------
    G : NetworkX graph
    T : Prim's Algorithm
    
    Returns
    -------
    The edge with the lowest cost/weight.
    """
    edge_list = possible_edges(G, T)
    edge_list.sort(key = lambda e : cost(G, e))
    return edge_list[0]
