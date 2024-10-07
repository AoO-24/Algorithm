from collections import deque

def BFS(tree, root):
    # TODO: implement BFS for the given tree, starting at node `root`
    visited = set() # set
    visited_order = [] # list
    tree_deque = deque()

    tree_deque.append(root)

    while tree_deque:
        cur = tree_deque.popleft()
        visited_order.append(cur)

        for sub in tree[cur]:
            if sub not in visited:
                tree_deque.append(sub)

        visited.add(cur)


    # TODO: return the list of tree nodes in the order they were visited
    return visited_order

tree = {
    'computer' : ['printer', 'router'],
    'printer' : ['paper', 'computer'],
    'router' : ['internet', 'computer'],
    'internet' : ['data', 'router'],
    'paper' : ['printer'],
    'data' : ['internet'],
}

print(BFS(tree, 'computer')) # Change 'computer' to starting node of your choice