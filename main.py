from graph1 import Graph
from hamiltonian import *
from fleury import *
import hierholzer as h

if __name__ == '__main__':

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

	fleury_circuit = {(0, 1), (0, 2),
					  (1, 0), (1, 2),
					  (2, 0), (2, 1), (2, 3),
					  (3, 2)}

	
	test2 = {(1,2), (1,3), (1,4), (1,5), (2,3), (2,1), (3, 4), (3, 1)}
	
	graph = Graph(hamiltonian_circuit)	

	eulerian = h.eulerian_path(eurilian_trail)
	print 'Heulerian Path:', eulerian
	
	hamiltonian_path = hamiltonian(graph)
	if(hamiltonian_path):
		print 'Hamiltonian:', hamiltonian_path

	print 'Fleury:', fleury(fleury_circuit)