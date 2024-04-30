from main import bfs
from edgegraph import GraphEL, VertexEL, EdgeEL, parse_graph_file

graph = GraphEL()
start_vertex = VertexEL("A")
graph.add_vertex(start_vertex)
graph.add_edge(EdgeEL("AB", start_vertex, VertexEL("B")))
graph.add_edge(EdgeEL("AC", start_vertex, VertexEL("C")))
graph.add_edge(EdgeEL("BD", VertexEL("B"), VertexEL("D")))
graph.add_edge(EdgeEL("CE", VertexEL("C"), VertexEL("E")))
bfs_order = bfs(graph, start_vertex)
print(bfs_order)

