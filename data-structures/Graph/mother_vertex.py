from Graph.graph import Graph
from Stack.stack import MyStack
# We only need Graph and Stack for this question!


def find_mother_vertex(g):
    # Traverse the Graph Array and perform DFS operation on each vertex
    # The vertex whose DFS Traversal results is equal to the total number
    # of vertices in graph is a mother vertex
    num_of_vertices_reached = 0
    for i in range(g.vertices):
        num_of_vertices_reached = perform_DFS(g, i)
        if num_of_vertices_reached is g.vertices:
            return i
    return - 1

    # Performs DFS Traversal on graph starting from source
    # Returns total number of vertices which can be reached from source


def perform_DFS(g, source):
    num_of_vertices = g.vertices
    vertices_reached = 0  # To store how many vertices reached from source

    # A list to hold the history of visited nodes (by default all false)
    # Make a node visited whenever you push it into stack
    visited = [False] * num_of_vertices

    # Create Stack (Implemented in previous section) for Depth First Traversal
    # and Push source in it
    stack = MyStack()
    stack.push(source)
    visited[source] = True
    # Traverse while stack is not empty
    while stack.is_empty() is False:
        # Pop a vertex/node from stack
        current_node = stack.pop()
        # Get adjacent vertices to the current_node from the list,
        # and if only push unvisited adjacent vertices into stack
        temp = g.array[current_node].head_node
        while temp is not None:
            if visited[temp.data] is False:
                stack.push(temp.data)
                visited[temp.data] = True
                vertices_reached += 1
            temp = temp.next_element
        # end of while
    return vertices_reached + 1  # +1 is to include the source itself




# def find_mother_vertex(g):
#     # visited[] is used for DFS. Initially all are
#     # initialized as not visited
#     visited = [False]*(g.vertices)
#
#     # To store last finished vertex (or mother vertex)
#     last_v = 0
#
#     # Do a DFS traversal and find the last finished
#     # vertex
#     for i in range(g.vertices):
#         if visited[i] is False:
#             perform_DFS(g, i, visited)
#             last_v = i
#
#     # If there exist mother vertex (or vetices) in given
#     # graph, then v must be one (or one of them)
#
#     # Now check if v is actually a mother vertex (or graph
#     # has a mother vertex). We basically check if every vertex
#     # is reachable from v or not.
#
#     # Reset all values in visited[] as false and do
#     # DFS beginning from v to check if all vertices are
#     # reachable from it or not.
#     visited = [False]*(g.vertices)
#     perform_DFS(g, last_v, visited)
#     if any(i is False for i in visited):
#         return -1
#     else:
#         return last_v
#
#
# # A recursive function to print DFS starting from v
# def perform_DFS(g, node, visited):
#
#     # Mark the current node as visited and print it
#     visited[node] = True
#
#     # Recur for all the vertices adjacent to this vertex
#     temp = g.array[node].head_node
#     while(temp):
#         if visited[temp.data] is False:
#             perform_DFS(g, temp.data, visited)
#         temp = temp.next_element


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 0)
g.add_edge(3, 1)
print(find_mother_vertex(g))