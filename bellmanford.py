#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:18:48 2023

@author: shashankramachandran
"""




import sys
import os
import heapq
import queue
import numpy as np
import simplegraphs as sg




def bellmanFordSimple(G, s):
    # G is a dictionary with keys "n", "m", "adj" representing an *weighted* graph
    # G["adj"][u][v] is the cost (length / weight) of edge (u,v)
    # This algorithms finds least-costs paths to all vertices
    # Will not detect negative-cost cycles
    # Returns an dict of distances (path costs) and parents in the lightest-paths tree.
    #
    # This is basically the algorithm we covered in class (except it
    # finds paths from a source instead of to a desitnation).
    #
    n = G["n"]
    d = [{} for i in range(n + 1)]
    for u in G["adj"]:
        d[0][u] = np.inf
    d[0][s] = 0
    parent = {s: None}
    for i in range(1,n+1):
        changed = False
        for v in G["adj"]:
            d[i][v] = d[i-1][v]
        for u in G["adj"]:
            for v in G["adj"][u]:
                newlength = d[i-1][u] + G["adj"][u][v]
                if newlength <  d[i][v]:
                    d[i][v] = newlength
                    parent[v] = u
                    changed = True
        # How can you decide whether it is ok to stop?
    if changed:
        print("Negative cycle reachable from source!")
    distances = d[n-1] # If there are no negative-cost cycles, these are the correct distances. 
    return distances, parent


def findClosestNodes(G):
    # G is a dictionary with keys "n", "m", "adj" representing an *weighted* graph
    # G["adj"][u][v] is the cost (length / weight) of edge (u,v)
    #
    distances_to_closest = {}
    changed = False 
    n = G["n"]
    t = [{} for i in range(n+1)]
    for j in G["adj"]:
        t[j][0] = np.inf
    
    for i in range(1,(len(G["adj"])+1)):
        changed = False
        for u in G["adj"]:
            t[u][i] = t[u][i-1]
            for v in G["adj"][u]:
                c = G["adj"][u][v]
                temp = min(c,c+t[v][i-1])
                if temp < t[u][i]:
                    t[u][i] = temp 
                    changed = True
        if(changed == False):
            for x in G["adj"]:
                distances_to_closest[x] = t[x][i]
            return distances_to_closest
    
    if changed :
        print("Negative cycle reachable from source!")
    for x in G["adj"]:
        l = len(G["adj"])
        distances_to_closest[x] = t[x][l]
    return distances_to_closest
  
       

def writeBFOutput(distances, parent, out_file_name):
    # Assumes parents and distances have the same keys.
    # Prints a file with one line per node, of the form "node, distance, parent"
    with open(out_file_name, 'w') as f:
        for u in distances:
            f.write("{}, {}, {}\n".format(u, distances[u], parent[u]))
    return

def writeCNDistances(distances_to_closest, out_file_name):
    # Prints a file with one line per node, of the form "node, distance to closest node"
    with open(out_file_name, 'w') as f:
        L = list(distances_to_closest.keys())
        L.sort()
        for u in L:
            f.write("{}, {}\n".format(u, distances_to_closest[u]))
    return


def main(args = []):
    if len(args) < 3:
        print("Too few arguments! There should be at least 3.")
        return
    task = args[0]
    graph_file_name = args[1]
    out_file_name = args[2]
    if task == "shortestPaths":
        if len(args) != 4:
            print("Problem! There were {} arguments instead of 4 for Shortest Paths.".format(len(args)))
            return
        G = sg.readGraph(graph_file_name) # Read the graph from disk
        s = int(args[3])
        distances, parent = bellmanFordSimple(G,s)
        writeBFOutput(distances, parent, out_file_name)
    elif task == "closestNodes":
        if len(args) != 3:
            print("Problem! There were {} arguments instead of 3 for Shortest Paths.".format(len(args)))
        G = sg.readGraph(graph_file_name) # Read the graph from disk
        distances_to_closest = findClosestNodes(G)
        # We ignore the names of closest nodes and the first step
        writeCNDistances(distances_to_closest, out_file_name)
    else: 
        print("Problem! Task {} not recognized".format(task))
    return

if __name__ == "__main__":
    main(sys.argv[1:])    

