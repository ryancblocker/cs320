from util import cost, best_path, valid_path
from two_opt import two_opt


def ga_tsp(initial_population, distances, generations):
    if (initial_population is None or distances is None or generations is None):
        return None
    if not valid_path(initial_population):
        return None
    if generations <= 0:
        return None

    path = best_path(initial_population, distances)
    trial = 0
    while trial < generations:
        new_path = two_opt(path, distances)
        if not valid_path(new_path):
            return None
        path = new_path
        trial += 1
    return path
