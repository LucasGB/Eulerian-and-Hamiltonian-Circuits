from collections import deque
from graph1 import Graph
from collections import defaultdict

def pick_any(iterable):
    """Return any item from iterable, or raise StopIteration if empty."""
    return next(iter(iterable))

class NoEulerianPath(Exception):
    """Exception raised when there is no Eulerian path."""

def eulerian_path(edges):
    """Return an Eulerian path in the directed graph with the given
    iterable of edges, or raise NoEulerianPath if there is no such path.
    """
    graph = Graph(edges)

    # Mapping from surplus of out-edges over in-edges to list of nodes
    # with that surplus.
    surplus = defaultdict(list)
    for node in graph:
        in_degree = graph.in_degree(node)
        out_degree = graph.out_degree(node)
        degree_surplus = out_degree - in_degree
        if abs(degree_surplus) > 1:
            raise NoEulerianPath("Node {} has in-degree {} and out-degree {}."
                                 .format(node, in_degree, out_degree))
        surplus[degree_surplus].append(node)

    # Find the starting point for the path.
    if len(surplus[1]) == len(surplus[-1]) == 0:
        # Any starting point will do.
        start = pick_any(graph)
    elif len(surplus[1]) == len(surplus[-1]) == 1:
        # Must start at a node with more out- than in-neighbours.
        start = pick_any(surplus[1])
    else:
        raise NoEulerianPath("Graph has {} odd-degree nodes."
                             .format(len(surplus[1]) + len(surplus[-1])))

    # We'll be following a series of edge-disjoint paths in the graph.
    # This is a mapping from a node to a deque of the paths starting
    # at that node, each path being a list of nodes. (The reason for
    # using a deque is so that we can process these paths in the order
    # that they were found.)
    paths = defaultdict(deque)

    # Nodes that have been visited but have unvisited out-neighbours.
    unfinished = set([start])

    while unfinished:
        # Pick any unfinished node to start the current path.
        node = pick_any(unfinished)
        path = [node]
        paths[node].append(path)

        # Keep choosing any neighbour and removing the edge just
        # traversed, until a dead end is reached.
        while graph.out_degree(node):
            neighbour = pick_any(graph.out_neighbours(node))
            graph.remove_edge(node, neighbour)
            if graph.out_degree(node) == 0:
                unfinished.remove(node)
            path.append(neighbour)
            unfinished.add(neighbour)
            node = neighbour
        else:
            unfinished.remove(node)

    # If there are any edges remaining, that means the graph was
    # disconnected.
    if any(graph.degree(node) for node in graph):
        raise NoEulerianPath("Graph is not connected.")

    # Concatenate the individual paths into one continuous path (using
    # the "stack of iterators" pattern).
    path = []
    stack = [iter(paths[start].popleft())]
    while stack:
        for node in stack[-1]:
            if paths[node]:
                stack.append(iter(paths[node].popleft()))
                break
            else:
                path.append(node)
        else:
            stack.pop()

    # Check that we concatenated all the paths.
    assert not any(paths.values())

    return path