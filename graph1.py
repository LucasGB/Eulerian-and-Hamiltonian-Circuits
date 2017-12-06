from collections import defaultdict

class Graph:
    """A directed graph whose nodes are any hashable objects."""

    def __init__(self, edges=()):
        """Create a directed graph from an iterable of edges."""
        self._nodes = set() # Set of nodes.
        self._out = defaultdict(set) # Map from node to set of out-neighbours.
        self._in = defaultdict(set) # Map from node to set of in-neighbours.
        self.edges = edges

        for m, n in self.edges:
            self.add_edge(m, n)

    def __iter__(self):
        """Iterating over the graph yields its nodes."""
        return iter(self._nodes)

    def get_size(self):
        return  len(self._nodes)

    def get_edge_size(self):
        return len(self.edges)

    def add_edge(self, m, n):
        """Add an edge from m to n."""
        self._nodes.add(m)
        self._nodes.add(n)
        self._out[m].add(n)
        self._in[n].add(m)

    def remove_edge(self, m, n):
        """Remove the edge from m to n."""
        self._out[m].remove(n)
        self._in[n].remove(m)

    def out_neighbours(self, node):
        """Return the set of out-neighbours of a node."""
        return self._out[node]

    def in_degree(self, node):
        """Return the number of edges ending at node."""
        return len(self._in[node])

    def out_degree(self, node):
        """Return the number of edges starting at node."""
        return len(self._out[node])

    def degree(self, node):
        """Return the number of edges incident to node in either direction."""
        return self.in_degree(node) + self.out_degree(node)

    def print_graph(self):
        for node in self._nodes:            
            print '%s -> %s' % (node, self._out[node])