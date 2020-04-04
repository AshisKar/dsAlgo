from Graph.graph import Graph
from Stack.stack import MyStack


def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    # Alist to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Create Q(implemented in previous lesson) for Breadth First Traversal and enqueue source in it
    stack = MyStack()
    stack.push(source)
    visited.insert(source, True)

    # Traverse while queue is not empty
    while not stack.is_empty():
        # Dequeue a vertex/node from queue and add it to result
        current_node = stack.pop()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Q
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                stack.push(temp.data)
                visited[temp.data] = True  # Visit the current Node
            temp = temp.next_element
    return result


g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
print(dfs_traversal(g, 1))