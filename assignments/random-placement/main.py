import random
def placement(num_objects, map):
    avaliability_map = [[True] * len(map[0]) for i in range(len(map))]
    
    def is_available(x, y):
        if (avaliability_map[x][y]):
            return True
        else:
            return False

    def find_open_spaces(map):
        open_spaces = []
        for x in range(0, len(map)):
            for y in range(0, len(map)):
                if (is_available(x, y)):
                    open_spaces.append((x, y))
        return open_spaces

    def shuffle(open_spaces):
        random_element = (0, 0)
        for i in range(0, len(open_spaces)):
            if i == 0:
                j = random.randint(0, len(open_spaces) - 1)
            elif i == len(open_spaces) - 1:
                j = random.randint(0, i - 1)
            else:
                j = random.randint(0, i)
            temp = open_spaces[j]
            open_spaces[j] = open_spaces[i]
            open_spaces[i] = temp
            random_element = temp
        return random_element

    def select_spaces(num_objects, map):
        objects_left = num_objects
        random_spaces = []
        while objects_left > 0:
            open_spaces = find_open_spaces(map)
            current_space = shuffle(open_spaces)    
            avaliability_map[current_space[0]][current_space[1]] = False
            random_spaces.append(current_space)
            objects_left -= 1
        print(avaliability_map)
        return random_spaces
            
    if map is None:
        return None
    if not isinstance(map, list):
        return None
    if num_objects is None:
        return None
    if len(map) == 1 and len(map[0]) == 1:
        return None
    if not isinstance(num_objects, int):
        return None
    if num_objects > len(map) * len(map[0]):
        return None

    return select_spaces(num_objects, map)
