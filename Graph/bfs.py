from Graph.graph import Graph
from Q.queue import MyQueue


def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    # Alist to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Create Q(implemented in previous lesson) for Breadth First Traversal and enqueue source in it
    queue = MyQueue()
    queue.enqueue(source)
    visited.insert(source, True)
    # Traverse while queue is not empty
    while not queue.is_empty():
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Q
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True  # Visit the current Node
            temp = temp.next_element
    return result


g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
print(bfs_traversal(g, 1))
# g = Graph(6)
#
# num_of_vertices = g.vertices
#
# if num_of_vertices == 0:
#     print("Graph is empty")
# else:
#     g.add_edge(0, 1)
#     g.add_edge(0, 2)
#     g.add_edge(1, 3)
#     g.add_edge(2, 3)
#
#     print(bfs_traversal(g, 0))
