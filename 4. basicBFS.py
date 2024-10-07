from collections import deque

def BFS(tree, root):
    visited = set() # set
    visited_order = [] #list
    queue = deque() #list

    queue.append(root)

    while queue:
        node = queue.popleft()
        visited_order.append(node)
        visited.add(node)

        # Now add all unvisited children to the queue 
        # tree[] is a dictionary that contain every node's suburban arraies as list

        for child in tree[node]:
            if child not in visited:
                queue.append(child)

        return visited_order 
        # It's a List