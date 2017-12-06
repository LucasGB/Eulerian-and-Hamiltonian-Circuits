#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import copy

def find_all_paths(graph, start, end, path=[]):
        #http://www.python.org/doc/essays/graphs/
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def find_paths(graph):
    cycles=[]
    for startnode in graph:
        for endnode in graph:
            newpaths = find_all_paths(graph, startnode, endnode)
            for path in newpaths:
                if (len(path)==len(graph)):                    
                    cycles.append(path)
    return cycles

def find_cycle(graph):
    cycles=[]
    for startnode in graph:
        for endnode in graph:
            newpaths = find_all_paths(graph, startnode, endnode)
            for path in newpaths:
                if (len(path)==len(graph)):
                    if path[0] in graph[path[len(graph)-1]]:
                        #print path[0], graph[path[len(graph)-1]]
                        path.append(path[0])
                        cycles.append(path)
    return cycles

def hamiltonian(graph):

    print "Finding Hamiltonian Paths----"
    
    a= find_paths(graph)
    
    ##for any in a:
    ##    for d in any:
    ##        print d, "->",
    
    print "Number of Hamiltonian Paths=", len(a)
    print "Finding Hamiltonian Cycles----"
    a= find_cycle(graph)
    
    if (a ==[]):
        print "No Hamiltonian Cycle"
    else:
        for any in a:
            for d in any:
                print d, "->",
            print
    
    print "Number of Hamiltonian Cycles=", len(a)
    #Visualize
    # http://ashitani.jp/gv/
    G=graph
    f = open('dotgraph.txt','w')
    f.writelines('digraph G {\nnode [width=.3,height=.3,shape=octagon,style=filled,color=skyblue];\noverlap="false";\nrankdir="LR";\n')
    f.writelines
    for i in G:
        for j in G[i]:
            s= '      '+ i
            s +=  ' -- ' +  j 
            s+=';\n'
            f.writelines(s)
            G[j].remove(i)
        
    
    f.writelines('}')
    f.close()
    print "done!"

def is_connected(G):
    start_node = list(G)[0]
    color = {v: 'white' for v in G}
    color[start_node] = 'gray'
    S = [start_node]
    while len(S) != 0:
        u = S.pop()
        for v in G[u]:
            if color[v] == 'white':
                color[v] = 'gray'
                S.append(v)
            color[u] = 'black'
    return list(color.values()).count('black') == len(G)

def from_dict(G):
    links = []
    for u in G:
        for v in G[u]:
            links.append((u,v))
    return links

'''
    odd_degree_nodes - returns a list of all G odd degrees nodes
'''
def odd_degree_nodes(G):
    odd_degree_nodes = []
    for u in G:
        if len(G[u]) % 2 != 0:
            odd_degree_nodes.append(u)
    return odd_degree_nodes

'''
Returns a list of odd degree vertexes
'''
def get_odd_degree_vertexes(graph):
    odd_nodes = []
    for vertex in graph:
        if(len(graph[vertex]) % 2 != 0):
            odd_nodes.append(vertex)
    print odd_nodes
    return odd_nodes

'''
Returns true if there are edges left in the graph
'''
def has_edges(graph):
    if(sum(len(v) for v in graph.itervalues()) == 0):
        return False
    else:
        print sum(len(v) for v in graph.itervalues())
        return True

def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
            it, i.e. the number of adjacent vertices. Loops are counted 
            double, i.e. every occurence of vertex in the list 
            of adjacent vertices. """ 
        adj_vertices =  self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

def remove_edge(graph, u, v):
    return graph[graph[u].pop(v)]

def fleury(graph):
    odd_vertexes = get_odd_degree_vertexes(graph)

    if(len(odd_vertexes) != 0 and len(odd_vertexes) != 2):
        print 'Não é um grafo euriliano!'
        print len(odd_vertexes)
    else:
        if(len(odd_vertexes) == 0):
            start = graph.keys()[0]
        else:
            start = odd_vertexes[0]
        
        #while(has_edges(graph)):
        #has_edges(graph.keys()[0])
        print graph[start]
        print vertex_degree(graph[start])
        #print 'dasd', remove_edge(graph, start, 2)
    

def eurilian1(graph):
    odn = odd_degree_nodes(graph)

    if len(odn) > 2 or len(odn) == 1:
        return 'Não é um grafo euriliano!'
    else:
        g = copy(graph)
        trail = []
        if len(odn) == 2:
            u = odn[0]
        else:
            u = list(g)[0]
        while len(from_dict(g)) > 0:
            current_vertex = u
            for u in g[current_vertex]:
                g[current_vertex].remove(u)
                g[u].remove(current_vertex)
                bridge = not is_connected(g)
                if bridge:
                    g[current_vertex].append(u)
                    g[u].append(current_vertex)
                else:
                    break
            if bridge:
                g[current_vertex].remove(u)
                g[u].remove(current_vertex)
                g.pop(current_vertex)
            trail.append((current_vertex, u))
    return trail

if __name__ == "__main__":
    
    ##graph = {'1': ['2', '4'],
    ##             '2': ['1', '3','5'],
    ##             '3': ['2','4'],
    ##             '4': ['1','3','5'],
    ##             '5': ['2','4']}
    graph = {'1': ['2', '4','5'],
                 '2': ['1', '3','5'],
                 '3': ['2','5','6'],
                 '4': ['1','7','5'],
                 '5': ['1','2','3', '4','6','7','8','9'],
                 '6': ['3','5','9'],
                 '7': ['4','5','8'],
                 '8': ['7','5','9'],
                 '9': ['8','5','6']}
    koningsberg = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 1, 3], 3: [0, 1, 2]}
    eurilian_trail = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}

    test = {'A': ['B', 'C', 'E'],
            'B': ['A', 'C', 'D'],
            'C': ['A', 'B', 'D', 'F'],
            'D': ['B', 'C', 'F'],
            'E': ['A', 'F'],
            'F':['C', 'D', 'E']}

    print fleury(test)