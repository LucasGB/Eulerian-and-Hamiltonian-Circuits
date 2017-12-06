from graph1 import Graph
import hierholzer as h


if __name__ == '__main__':
	test = {'A': ['B', 'C', 'E'],
            'B': ['A', 'C', 'D'],
            'C': ['A', 'B', 'D', 'F'],
            'D': ['B', 'C', 'F'],
            'E': ['A', 'F'],
            'F':['C', 'D', 'E']}

	eurilian_trail = {(1, 2), (1, 3),
				   (2, 1), (2, 3), (2, 4),
				   (3, 1), (3, 2), (3, 4),
				   (4, 2), (4,3)}
	hey = {(0, 1), (0, 2), (0, 3),
		   (1, 0), (1, 2),
		   (2, 0), (2, 1),
		   (3, 0), (3, 4)}
	
	test2 = {(1,2), (1,3), (1,4), (1,5), (2,3), (2,1), (3, 4), (3, 1)}
	path = h.eulerian_path(hey)
	print path
	#g = Graph({(1,2), (1,3), (1,4), (1,5), (2,3), (2,1), (3, 4), (3, 1)})
	#g.print_graph()
	
	#print 'dmas,', max(g.out_neighbours(1), key=g.degree)