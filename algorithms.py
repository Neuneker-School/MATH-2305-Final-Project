# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:54:45 2020

@authors: Jeremiah Neuneker, Julia Ramirez, Warda Qadeer, Noah V.
"""

from functions import min_cost_edge, prims_initialize, is_spanning, E, cost
from drawing import show_weighted_graph, draw_subtree

def prims_algorithm(G, starting_vertex, show_graph = False, show_cost = False):
    """Primary execution function for solving Prims Algorithm 
    
    Parameters
    ----------
    G : NetworkX graph
    starting_vertex : the vertex to use as a starting point
    show_graph : should the graph be rendered
    show_cost : should the cost of the tree be output
    
    Returns
    -------
    The resulting graph
    """
    if show_graph == True:
        show_weighted_graph(G)
        
    T = prims_initialize(G, starting_vertex)
    
    if show_graph == True:
        draw_subtree(G, T)
        
    while is_spanning(G, T) == False:
        e = min_cost_edge(G, T)
        T.add_edge(e[0], e[1])
        if show_graph == True:
            draw_subtree(G, T)
    if show_cost == True:
        c = sum([cost(G,e) for e in E(T)])
        print(f'The cost of this spanning tree is {c}')
        
    return T
    
