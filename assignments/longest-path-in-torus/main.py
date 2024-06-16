def longest_path(torus):
    if torus is None or not torus[0]:
        return []
    
    if not isinstance(torus[0], list):
        return None

    for row in torus:
        if not isinstance(row, list):
            return None
        
    if len(row) != len(torus[0]):
            return None

    if not isinstance(torus, list):
        return None
    
    if len(torus) == 1:
        return [(0, 0)]
    if len(torus[0]) == 1:
        return [(0, 0)]

    num_rows = len(torus)
    num_cols = len(torus[0])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_path_length = 0
    max_path = []

    for i in range(num_rows):
        for j in range(num_cols):
            queue = [(i, j, [(i, j)])]
            front = 0
            while front < len(queue):
                x, y, path = queue[front]
                front += 1
                for dx, dy in directions:
                    new_x = (x + dx) % num_rows
                    new_y = (y + dy) % num_cols
                    if torus[new_x][new_y] > torus[x][y]:
                        new_path = path + [(new_x, new_y)]
                        queue.append((new_x, new_y, new_path))
                        if len(new_path) > 1 and len(new_path) > max_path_length:
                            max_path_length = len(new_path)
                            max_path = new_path
                        elif len(new_path) == max_path_length:
                            max_path = new_path

    if not max_path:
        return []
    return max_path
