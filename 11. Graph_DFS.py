def DFS(graph, start, visited=None):
    # When start before recursive call, we do initialization.
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for next_node in graph[start]:
        if next_node not in visited:
            DFS(graph, next_node, visited)

'''

Key Concept:
0. Initialize 'visited' as set if None

1. Mark the current node as 'visited' and print the node.

2. For every adjacent unvisited node of the current node:

    2.1. Invoke the recursive DFS function.
    
'''

graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A']),
    'D': set(['B']),
    'E': set(['B']),
}

DFS(graph, 'A')  # Output: A B D E C
