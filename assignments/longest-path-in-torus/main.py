def longest_path(torus):

    num_rows = len(torus)
    num_cols = len(torus[0])
    
    def is_valid(torus, x, y, value):
        x = x % num_rows
        y = y % num_cols
        return torus[x][y] > value
    
    def longest_path_from_cell(torus, x, y, cache):
        x = x % num_rows
        y = y % num_cols

        if cache[x][y] != -1:
            return cache[x][y]
        
        result = 1
        value = torus[x][y]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            dir_row, dir_col = direction
            nx = x + dir_row
            ny = y + dir_col

            if is_valid(torus, nx, ny, value):
                result = max(result, 1 + longest_path_from_cell(torus, nx, ny, cache))
        
        cache[x][y] = result
        return result
    
    def longest_path(torus):
        if torus or not torus[0]:
            return []
        
        cache = [[-1] * num_cols for _ in range(num_rows)]
        
        start_cell = None
        max_length = 0

        for x in range(num_rows):
            for y in range(num_cols):
                length = longest_path_from_cell(torus, x, y, cache)

                if length > max_length:
                    max_length = length
                    start_cell = (x, y)

        if not start_cell:
            return []
        
        path = [start_cell]
        value = torus[start_cell[0]][start_cell[1]]

        while len(path) < max_length:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction in directions:
                dir_row, dir_col = direction
                nx = path[-1][0] + dir_row
                ny = path[-1][1] + dir_col

                if is_valid(torus, nx, ny, value):
                    path.append((nx, ny))
                    value = torus[nx][ny]
                    break
        return path
    
    return longest_path(torus)
   