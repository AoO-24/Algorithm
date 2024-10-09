
'''
Initialize an empty Queue Q

Mark the starting vertex as visited and enqueue it into Q

WHILE Q is not empty DO
    Dequeue a vertex (say V) from Q
    FOR each neighbor (say N) of V DO
        IF N is not visited
            Mark N as visited and enqueue it into Q
        END IF
    END FOR
END WHILE
'''



from collections import deque

def BFS(graph, start):
    visited = set([start])   # a set to keep track of visited nodes
    queue = deque([start])  # a deque (double-ended queue) to manage BFS operations

    while queue:
        node = queue.popleft()  # dequeue a node
        print(node, end=" ")  # Output the visited node

        for neighbor in graph[node]:  # visit all the neighbors
            if neighbor not in visited:  # enqueue unvisited neighbors
                queue.append(neighbor)
                visited.add(neighbor)  # mark the neighbor as visited

# Use an adjacency list to represent the graph
graph = {'A': ['B', 'D'], 'B': ['A', 'C', 'F'], 'C': ['B'], 'D': ['A', 'E'], 'E': ['D'], 'F': ['B']}

BFS(graph, 'A')  # Call the BFS function

# Output: A B D C F E