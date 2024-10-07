class Area:
    def __init__(self, name):
        self.name = name
        self.sub_area = []

    def add_subarea(self, name):
        self.sub_area.append(Area('name'))

def DFS(self, visited = None):
    if visited is None:
        visited = set()
    print(self.name)
    visited.add(self)
    for sub in self.sub_area:
        if sub not in visited:
            sub.DFS(visited)


NY = Area('NY')
NY.add_subarea("GA")
NY.add_subarea('PA')
NY.add_subarea('PA')
NY.add_subarea('NJ')
GA.add_subarea('MI')

NY.DFS()
