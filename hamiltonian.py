import random
from graph import Graph

"""Return any item from iterable, or raise StopIteration if empty."""
def pick_any(iterable):
    return next(iter(iterable))

"""Performs a recursive Bread-First-Search on the graph structure while keeping an unvisited list to avoid visiting vertexes more than once. If the size of the path discovered by the algorithm is equal to the graph's number of vertexes and the last visited vertex has transition to the root, then a hamiltonian circuit has been identified."""
def BFS(graph, start, goal, path):
    current_node = start

    # Removes transitions to vertices that have been visited
    unvisited = graph.out_neighbours(current_node) - set(path)

    # If there are vertices that haven't been visited yet
    if(len(unvisited) != 0):
        for node in graph.out_neighbours(current_node) - set(path):
            path.append(node)
            return BFS(graph, node, goal, path)

    # If the stop criteria has been reached, return the path
    elif(len(path) == graph.get_size() and goal in graph.out_neighbours(current_node)):
        path.append(goal)
        return path

    else:
        return None

"""Selects a random vertex to start the algorithm and calls BFS"""
def hamiltonian(edges):
    graph = Graph(edges)

    start = next(iter(graph))
    end = start
    path = [start]    

    return BFS(graph, start, end, path)