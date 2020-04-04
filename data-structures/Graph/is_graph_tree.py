from Graph.graph import Graph
# We only need Graph for this Question!


def is_tree(g):
    # All vertices unvisited
    visited = [False] * g.vertices

    # Check cycle using recursion stack
    # Also mark nodes visited to check connectivity
    if check_cycle(g, 0, visited, -1) is True:
        return False

    # Check if all nodes we visited from the source (graph is connected)
    for i in range(len(visited)):
        # Graph is not connected
        if visited[i] is False:
            return False
    # Not cycle and connected graph
    return True


def check_cycle(g, node, visited, parent):
    # Mark node as visited
    visited[node] = True

    # Pick adjacent node and run recursive DFS
    adjacent = g.array[node].head_node
    while adjacent:
        if visited[adjacent.data] is False:
            if check_cycle(g, adjacent.data, visited, node) is True:
                return True

        # If adjacent is visited and not the parent node of the current node
        elif adjacent.data is not parent:
            # Cycle found
            return True
        adjacent = adjacent.next_element

    return False


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(3, 4)
g.add_edge(1, 0)
g.add_edge(2, 0)
g.add_edge(3, 0)
g.add_edge(4, 3)

print(is_tree(g))