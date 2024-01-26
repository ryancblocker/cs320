def repeats(lst):
    if lst is None or len(lst) < 2:
        return None

    for pattern_length in range(1, len(lst) // 2 + 1):
        if len(lst) % pattern_length == 0:
            pattern = lst[:pattern_length]
            if pattern * (len(lst) // pattern_length) == lst:
                return pattern
    return None
# # Test cases
# print(repeats(['a', 'b', 1, 'b', 'a', 'b', 1, 'b']))
# print(repeats(['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']))
# print(repeats(['a', 'b', 'a', 'b', 'a', 'b', 'c']))
# print(repeats([1]))
# print(repeats(None))
