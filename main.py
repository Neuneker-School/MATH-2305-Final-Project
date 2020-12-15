# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:55:43 2020

@authors: Jeremiah Neuneker, Julia Ramirez, Warda Qadeer, Noah V.
"""
import networkx as nx
from algorithms import prims_algorithm
from functions import FileSelector, InputStartingPoint

def main():
    
    
    while True:
        inputFile = FileSelector('test-graphs/')
        
        graph_data = open(inputFile, 'r')
        
        G = nx.read_weighted_edgelist(graph_data, nodetype = int)
        
        startingVertex = InputStartingPoint(G)
        
        T = prims_algorithm(G, startingVertex, True, True)
        
        graph_data.close()
        
        
        if input('Would you like to solve another graph (y/n): ').upper() != 'Y':
            return
    
main()



    