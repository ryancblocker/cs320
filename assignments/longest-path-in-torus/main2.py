# A function to check if a cell is valid and has a greater value than the current cell
def is_valid(torus, x, y, value):
    # Get the dimensions of the torus
    m = len(torus)
    n = len(torus[0])
    # Wrap around the edges of the torus
    x = x % m
    y = y % n
    # Return true if the cell is valid and has a greater value
    return torus[x][y] > value

# A function to find the longest path from a given cell
def longest_path_from_cell(torus, x, y, cache):
    # Get the dimensions of the torus
    m = len(torus)
    n = len(torus[0])
    # Wrap around the edges of the torus
    x = x % m
    y = y % n
    # If the result is already cached, return it
    if cache[x][y] != -1:
        return cache[x][y]
    # Initialize the result as 1
    result = 1
    # Get the value of the current cell
    value = torus[x][y]
    # Try all four directions from the current cell
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        # Get the next cell coordinates
        nx = x + dx
        ny = y + dy
        # If the next cell is valid and has a greater value, update the result
        if is_valid(torus, nx, ny, value):
            result = max(result, 1 + longest_path_from_cell(torus, nx, ny, cache))
    # Cache the result for the current cell
    cache[x][y] = result
    # Return the result
    return result

# A function to find the longest path in the torus
def longest_path(torus):
    # If the torus is None or empty, return an empty list
    if not torus or not torus[0]:
        return []
    # Get the dimensions of the torus
    m = len(torus)
    n = len(torus[0])
    # Initialize the cache with -1
    cache = [[-1] * n for _ in range(m)]
    # Initialize the maximum length and the starting cell
    max_length = 0
    start_cell = None
    # Loop through all the cells in the torus
    for i in range(m):
        for j in range(n):
            # Find the longest path from the current cell
            length = longest_path_from_cell(torus, i, j, cache)
            # If the length is greater than the maximum length, update it and the starting cell
            if length > max_length:
                max_length = length
                start_cell = (i, j)
    # If there is no valid path, return an empty list
    if not start_cell:
        return []
    # Initialize the path with the starting cell
    path = [start_cell]
    # Get the value of the starting cell
    value = torus[start_cell[0]][start_cell[1]]
    # Loop until the path length is equal to the maximum length
    while len(path) < max_length:
        # Try all four directions from the current cell
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            # Get the next cell coordinates
            nx = path[-1][0] + dx
            ny = path[-1][1] + dy
            # If the next cell is valid and has a greater value, append it to the path and break
            if is_valid(torus, nx, ny, value):
                path.append((nx, ny))
                value = torus[nx][ny]
                break
    # Return the path
    return path
