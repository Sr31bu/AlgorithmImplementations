#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:08:45 2023

@author: shashankramachandran
"""


import sys
import numpy as np
import simplegraphs as sg


def shortestHole(G,s):
    found = False
    hole_length =  -1 # Default value for when no hole is found
    hole_nodes = [] # Default value for when no hole is found
    d, parent, layers = sg.BFS(G, s)
    firstNode = {}
    for u in layers[1]:
        firstNode[u] = u
    
    for i in range(2,len(layers)):
        for v in layers[i]:
            firstNode[v] = firstNode[parent[v]]
    
    sim_cyc_found = False
    sim_cyc_len = float("inf")
    for i in range(1,len(layers)):
        for u in layers[i]:
            for v in G["adj"][u]:
                if v != s and firstNode[v] != firstNode[u]:
                    sim_cyc_found = True
                    this_cyc_len =  d[u] + d[v] + 1
                    if this_cyc_len < sim_cyc_len :
                        sim_cyc_len = this_cyc_len
                        sim_cyc_edge = (u,v)
                        
    
    if sim_cyc_found:
        (u,v) = sim_cyc_edge
        part1 = find_path(parent, s, u)
        part2 = find_path(parent, s,v)
        part1.append(s)
        part1.reverse()
        sym_cyc_node = part1 + part2
        return True,sim_cyc_len,sym_cyc_node
    
        
        
                    

    # Return the output
    return found, hole_length, hole_nodes




def find_path(parent,s,u):
    path = []
    while u != s:
        path.append(u)
        u = parent[u]
    return path 
    


def readSource(start_file):
    # The source vertex is listed in its own file
    # It is an integer on a line by itself.
    with open(start_file, 'r') as f:
        raw_start = f.readline()
        s = int(raw_start)
    return s



def writeOutput(output_file, hole_found, hole_length, hole_list):
    # This takes the outputs of shortestHole and writes them
    # to a file with the name output_file
    with open(output_file, 'w') as f:
        f.write("{}\n".format(hole_found))
        f.write("{}\n".format(hole_length))
        f.write("{}\n".format(hole_list))
    return



def main(args=[]):
    # Expects three command-line arguments:
    # 1) name of a file describing the graph
    # 2) name of a file with the ID of the start node
    # 3) name of a file where the output should be written
    if len(args) != 3:
        print("Problem! There were {} arguments instead of 3.".format(len(args)))
        return
    graph_file = args[0]
    start_file = args[1]
    out_file = args[2]
    G = sg.readGraph(graph_file) # Read the graph from disk
    s = readSource(start_file) # Read the source from disk
    hole_found, hole_length, hole_list = shortestHole(G,s) # Find the shortest hole!
    writeOutput(out_file, hole_found, hole_length, hole_list) # Write the output
    return 

if __name__ == "__main__":
    main(sys.argv[1:])    

    