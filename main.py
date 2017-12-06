from graph1 import Graph
from hamiltonian import *
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
	
	euler_circuit = {(0, 1), (0, 2), (0, 3), (0, 4),
		   			 (1, 0), (1, 2),
		    		 (2, 0), (2, 1), (2, 5),
		   			 (3, 0), (3, 4),
		   			 (4, 0), (4, 3)}

	hamiltonian_circuit = {(0, 2), (0, 4),
		   			 (1, 3), (1, 4),
		    		 (2, 0), (2, 3),
		   			 (3, 1), (3, 2),
		   			 (4, 0), (4, 1)}

	
	test2 = {(1,2), (1,3), (1,4), (1,5), (2,3), (2,1), (3, 4), (3, 1)}
	
	graph = Graph(hamiltonian_circuit)

	graph.print_graph()

	#print 'Heulerian Path:', h.eulerian_path(eurilian_trail)
	#print 'Hamiltonian:', bfs(graph, 1, 1, [])
	f_path = bfs(graph, 0, 0, {0})
	print 'Final path:', f_path



	#g = Graph({(1,2), (1,3), (1,4), (1,5), (2,3), (2,1), (3, 4), (3, 1)})
	#g.print_graph()
	
	#print 'dmas,', max(g.out_neighbours(1), key=g.degree)