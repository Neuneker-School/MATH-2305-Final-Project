# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:55:37 2020

@authors: Jeremiah Neuneker, Julia Ramirez, Warda Qadeer, Noah V.
"""

import networkx as nx
from algorithms import prims_algorithm
from drawing import *
from functions import *
    
graph_data = open('test-graphs\g2.txt', 'r')
    
G = nx.read_weighted_edgelist(graph_data, nodetype = int)

T = prims_algorithm(G, 0, True, True)

graph_data.close()