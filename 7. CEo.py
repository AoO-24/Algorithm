from collections import deque

# Define BFS function
def BFS(graph, root):
    visited = [] # List to keep track of visited nodes
    queue = deque() # A queue to add nodes for visiting
    queue.append(root) # Start with the root node

    while queue: # While there are nodes to visit.
        vertex = queue.popleft() # Visit the first node in the queue.
        visited.append(vertex) # This mean we only consider this vertex into visited after or we gonna loop the vertex's graph[vertex] neighbor.
        # Now add all unvisited children to the queue
        for child in graph[vertex]:

            if child not in visited:
                queue.append(child)


    return visited

# Define the adjacency list of our graph
graph = {
    '1': ['2', '3', '4'],
    '2': ['1', '5', '6'],
    '3': ['1', '7', '8'],
    '4': ['1', '9', '10'],
    '5': ['2'],
    '6': ['2', '11'],
    '7': ['3'],
    '8': ['3'],
    '9': ['4'],
    '10': ['4'],
    '11': ['6']
}

# Call the BFS function
print(BFS(graph, '1'))