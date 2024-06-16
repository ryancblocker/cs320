from main import *
from edgegraph import *

# Create large graph
graph = GraphEL()
vertices = ['A', 'S', 'E', 'D', 'C', 'B']
for vertex in vertices:
    graph.add_vertex(VertexEL(vertex))

edges = [
    ('e1', 'A', 'S', 10),
    ('e2', 'A', 'E', 8),
    ('e3', 'E', 'D', 1),
    ('e4', 'D', 'C', 1),
    ('e5', 'C', 'B', 2),
    ('e6', 'S', 'C', 2),
    ('e7', 'B', 'S', 1),
    ('e8', 'D', 'S', 4),
]

for edge_id, tail, head, weight in edges:
    edge = EdgeEL(edge_id, graph.get_vertex(tail), graph.get_vertex(head))
    edge.set_value(weight)
    graph.add_edge(edge)
start_vertex = 'A'
end_vertex = 'C'
path = bellman_ford(graph, start_vertex, end_vertex)
print(f"Shortest path from {start_vertex} to {end_vertex}: {path}")

# test with only one vertices
graph = GraphEL()
vertices = ['A']
for vertex in vertices:
    graph.add_vertex(VertexEL(vertex))
    
edges = [
    ('e1', 'A', 'A', 1)
]

for edge_id, tail, head, weight in edges:
    edge = EdgeEL(edge_id, graph.get_vertex(tail), graph.get_vertex(head))
    edge.set_value(weight)
    graph.add_edge(edge)
start_vertex = 'A'
end_vertex = 'A'
path = bellman_ford(graph, start_vertex, end_vertex)
print(f"Shortest path from {start_vertex} to {end_vertex}: {path}")

