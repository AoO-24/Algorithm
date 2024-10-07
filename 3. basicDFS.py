class Area:
    def __init__(self, name):
        self.name = name
        self.sub_area = []

    def add_subarea(self, name):
        self.sub_area.append(Area(name))

    def dfs(self, visited = None):
        if visited is None:
            visited = set()
        print(self.name)
        visited.add(self)
        for sub in self.sub_area:
            if sub not in visited:
                sub.dfs(visited)


NY = Area('NY')
GA = Area('GA')
GA.add_subarea('NY')
NY.add_subarea("GA")
NY.add_subarea('PA')
NY.add_subarea('PA')
NY.add_subarea('NJ')
GA.add_subarea('MI')

NY.dfs()

print('-' * 50)

GA.dfs()