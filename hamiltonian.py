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
        print paths
        return paths

def find_paths(graph):
    cycles=[]
    for startnode in graph:
        for endnode in graph:
            print 'start', startnode
            print 'end', endnode
            newpaths = find_all_paths(graph, startnode, endnode)
            print newpaths
            for path in newpaths:
                print 'aqui',path
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

def bfs(graph, start, goal, path):
    current_node = start

    unvisited = graph.out_neighbours(current_node) - set(path)
    print 'PATH:', path
    print 'Unvisited:', unvisited

    if(len(unvisited) != 0):
        for node in graph.out_neighbours(current_node) - set(path):
            path.add(node)
            bfs(graph, node, goal, path)
    #else:
        #print 'path
        #bfs(graph, node, goal, path)

#        if(node == goal):
#            path.append(node)
#            print path
#        else:
#            bfs(graph, node, goal, path)

    