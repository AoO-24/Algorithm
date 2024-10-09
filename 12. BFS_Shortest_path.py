from collections import deque

def shortestPath(n, graph, start, end):
    # The queue stores tuples `(distance, path)`
    # where `distance` is the minimal distance to the current vertex
    # and `path` is the shortest path from the starting vertex to the current vertex
    queue = deque([(0, [start])])
    visited = set([start])
    min_distances = {start: 0}

    while queue:
        distance, path = queue.popleft()
        node = path[-1]
        min_distances[node] = distance

        if node == end:
            return distance, path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((distance + 1, path + [neighbor]))

    return float('inf'), []