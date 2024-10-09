class Area:
    def __init__(self, name):
        self.name = name
        self.sub_area = []

    def add_subarea(self, name):
        self.sub_area.append(Area(name))

    def dfs(self, visited = None):
        if visited is None:
            visited = set()

        visited.add(self)
        print(self.name)

        for sub in self.sub_area:
            if sub not in visited:
                sub.dfs(visited)

def DFS(node, visited = None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node.name)

    for sub in node.sub_area:
        if sub not in visited:
            sub.dfs(visited)
'''
The difference between this tree_DFS and Graph_DFS is tree restore adjacent list in 
Area's attribute.
 
Key Concept:
1. Mark the current node as 'visited' and print the node.

2. For every adjacent unvisited node of the current node:

    2.1. Invoke the recursive DFS function.
    
'''

NY = Area('NY')
GA = Area('GA')
GA.add_subarea('NY')
NY.add_subarea("GA")
NY.add_subarea('PA')
NY.add_subarea('NJ')
GA.add_subarea('MI')

print('-' * 50)

NY.dfs()

print('-' * 50)

GA.dfs()

print('-' * 50)

DFS(GA)

print('-' * 50)

DFS(NY)

print('-' * 50)
