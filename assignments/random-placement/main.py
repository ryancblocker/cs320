import random


def placement(num_objects, map):
    if num_objects <= 0 or map is None:
        return None
    
    num_rows = len(map)
    num_cols = len(map[0])

    def is_available(x, y):
        if (map[x][y]):
            return True
        else:
            return False
    
    open_spaces = []
    for x in range(num_rows):
        for y in range(num_cols):
            if (is_available(x, y)):
                open_spaces.append((x, y))
    
    free = len(open_spaces)
    if num_objects > free:
        return None
    
    def shuffle(spaces):
        for i in range(len(spaces) - 1, -1, -1):
            if i == 0:
                j = random.randint(0, len(spaces) - 1)
            else:
                j = random.randint(0, i)
            temp = spaces[j]
            spaces[j] = spaces[i]
            spaces[i] = temp
        return spaces
    
    shuffle(open_spaces)
    
    return open_spaces[:num_objects]
