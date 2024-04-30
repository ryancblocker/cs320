from collections import deque


def bfs(graph, start):
    if graph is None or start is None or start.name not in graph._vertices:
        return []
    visited = []
    queue = deque([start])
    visited_names = set([start.name])
    while queue:
        current = queue.popleft()
        visited.append(current)
        neighbors = []
        for edge in graph._edges.values():
            if current == edge._vertex1 and edge._vertex2.name not in visited_names:
                neighbors.append(edge._vertex2)
            elif current == edge._vertex2 and edge._vertex1.name not in visited_names:
                neighbors.append(edge._vertex1)
        for neighbor in neighbors:
            if neighbor.name not in visited_names:
                visited_names.add(neighbor.name)
                queue.append(neighbor)

    return visited
