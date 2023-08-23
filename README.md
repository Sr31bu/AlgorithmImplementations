# AlgorithmImplementations

Welcome to the **Algorithm Implementations** repository! This repository contains implementations of various algorithms in Python. Each set of code focuses on a specific algorithmic problem and provides a solution using Python programming.

## Set of Code 1: Stable Matching Algorithm Implementation

The first set of code implements the Stable Matching algorithm using the Gale-Shapley algorithm. This algorithm aims to find stable matches between two sets of participants based on their preferences.

### Contents:

1. `stable_matching.py`: The main script that implements the Gale-Shapley algorithm for stable matching.
2. `input_preferences_1.txt`: Sample input file containing preferences of two groups (hospitals and students).
3. `input_preferences_2.txt`: Sample input file containing preferences of two groups (companies and students).
4. `output_matches.txt`: Sample output file to store the matched pairs.

### Usage:

1. Run the script using the command: `python stable_matching.py input_preferences_1.txt input_preferences_2.txt output_matches.txt Q1`.
2. Replace `input_preferences_1.txt` and `input_preferences_2.txt` with your input files.
3. The `Q1` argument specifies the question to run (Q1, Q2, or Q3).

## Set of Code 2: Bellman-Ford Algorithm and Shortest Path Computation

The second set of code implements the Bellman-Ford algorithm to compute shortest paths in a weighted graph and find the closest nodes in terms of distance.

### Contents:

1. `shortest_path.py`: The main script that implements the Bellman-Ford algorithm and computes shortest paths.
2. `graph_input.txt`: Sample input file containing a weighted graph.
3. `output_shortest_paths.txt`: Sample output file to store shortest path results.
4. `output_closest_nodes.txt`: Sample output file to store closest nodes results.

### Usage:

1. Run the script for shortest paths: `python shortest_path.py shortest_paths graph_input.txt output_shortest_paths.txt`.
2. Run the script for closest nodes: `python shortest_path.py closest_nodes graph_input.txt output_closest_nodes.txt`.
3. Replace `graph_input.txt` with your input graph data file.

## Set of Code 3: Coffee Shop Server Arrangement Optimization

The third set of code focuses on optimizing the arrangement of servers in a coffee shop to maximize serving capacity while adhering to specific constraints.

### Contents:

1. `coffee_shop_optimization.py`: The main script for coffee shop server arrangement optimization.
2. `input_serving_capacities.txt`: Sample input file containing serving capacities of different locations.
3. `output_optimal_servers.txt`: Sample output file to store the list of optimal server positions.

### Usage:

1. Run the script: `python coffee_shop_optimization.py input_serving_capacities.txt output_optimal_servers.txt`.
2. Replace `input_serving_capacities.txt` with your input serving capacities file.

## Set of Code 4: Shortest Hole Detection in a Graph

The fourth set of code focuses on finding the shortest hole (symmetric cycle) in a graph starting from a specified source vertex.

### Contents:

1. `shortest_hole_detection.py`: The main script for detecting the shortest hole in a graph.
2. `graph_data.txt`: Sample input file containing graph data.
3. `source_vertex.txt`: Sample input file containing the source vertex.
4. `output_shortest_hole.txt`: Sample output file to store the shortest hole detection results.

### Usage:

1. Run the script: `python shortest_hole_detection.py graph_data.txt source_vertex.txt output_shortest_hole.txt`.
2. Replace `graph_data.txt` and `source_vertex.txt` with your input graph and source vertex files.

---
