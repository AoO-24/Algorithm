from collections import deque

def shortestPaths(n, graph, start):
    queue = deque([[start]])
    visited = set([start])
    shortest_paths = {start: [start]}

    # implement this
    

    return shortest_paths

# Test cases:

# We describe a simple graph with 3 nodes and 3 edges.
graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
print(shortestPaths(3, graph, 1))
# Expected output: {1: [1], 2: [1, 2], 3: [1, 3]}
# Explanation: The paths from node 1 to nodes 2 and 3 are direct edges.

graph = {1: [2], 2: [1, 3], 3: [2]}
print(shortestPaths(3, graph, 1))
# Expected output: {1: [1], 2: [1, 2], 3: [1, 2, 3]}
# Explanation: The path from node 1 to node 3 includes node 2, as there's no direct edge to node 3.

graph = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [1, 3]}
print(shortestPaths(4, graph, 1))
# Expected output: {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 4]}
# Explanation: There are direct edges from node 1 to all other nodes.