from edgegraph import *


def bellman_ford(graph, start, end):
    if graph is None or start is None or end is None:
        return []

    if not graph.get_vertex(start) or not graph.get_vertex(end):
        return []
    
    if len(graph.vertices()) == 1:
        return [start]

    distances = {vertex.name: float('inf') for vertex in graph.vertices()}
    predecessors = {}
    distances[start] = 0
    
    for vertex in range(len(graph.vertices()) - 1):
        for edge in graph.edges():
            if edge.get_value() <= 0:
                return []
            u = edge.tail().name
            v = edge.head().name
            weight = edge.get_value()
            
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
                
    if start == end:
        return [start]
       
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        if current_vertex == start:
            break
        current_vertex = predecessors[current_vertex]
    
    if path[-1] != start:
        return []
    
    return path[::-1]
