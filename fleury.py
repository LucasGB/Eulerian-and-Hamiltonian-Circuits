from graph1 import Graph
from collections import defaultdict

"""Return any item from iterable, or raise StopIteration if empty."""
def pick_any(iterable):
    return next(iter(iterable))

class NoEulerianPath(Exception):
    """Exception raised when there is no Eulerian path."""

def is_bridge(graph, node):
    if(len(graph.out_neighbours(node)) == 1):
        return True
    return False

"""Verifies if graph is made up by bridges only"""
def bridges_only(graph):
    for node in graph:
        if(graph.out_degree(node) > 1):
            return False
    return True

"""Removes the edge from the graph"""
def burn_edge(graph, u, v):
        graph.remove_edge(u, v)
        graph.remove_edge(v, u)
        return v

""""""
def fleury(edges):
    graph = Graph(edges)
    
    # Mapping from surplus of out-edges over in-edges to list of nodes
    # with that surplus.
    surplus = defaultdict(list)
    odd_degree_nodes = []
    for node in graph:
        in_degree = graph.in_degree(node)
        out_degree = graph.out_degree(node)
        degree_surplus = out_degree - in_degree

        if abs(degree_surplus) > 1:
            raise NoEulerianPath("Node {} has in-degree {} and out-degree {}."
                                 .format(node, in_degree, out_degree))

        surplus[degree_surplus].append(node)        
        if(len(graph.out_neighbours(node)) % 2 == 1):
            odd_degree_nodes.append(node)   

    if(len(odd_degree_nodes) != 0 and len(odd_degree_nodes) != 2):
        raise NoEulerianPath("Number of odd degree nodes is different than 0 or 2.")
    
    # If there are 0 odd vertices, start anywhere. If there are 2 odd vertices, start at one of them.
    if(len(odd_degree_nodes) == 0):
        node = pick_any(graph)
    else:
        node = pick_any(odd_degree_nodes)
    
    path = [node]

    while(graph.out_degree(node)):
        
        neighbour = None
        while(True):
            neighbour = pick_any(graph.out_neighbours(node))

            if(is_bridge(graph, neighbour) and bridges_only(graph)):
                path.append(burn_edge(graph, node, neighbour))
                break
            path.append(burn_edge(graph, node, neighbour))
            node = neighbour            

        while(is_bridge(graph, neighbour) and bridges_only(graph)):            
            neighbour = pick_any(graph.out_neighbours(neighbour))
            path.append(burn_edge(graph, node, neighbour))
            if(len(path) == graph.get_edge_size()):
                break
        break


    return path