def repeat(lst):
    if lst is None or not isinstance(lst, list):
        return None

    if len(lst) < 2:
        return None

    lst_length = len(lst)
    for pattern_length in range(lst_length // 2, 0, -1):
        if lst_length % pattern_length == 0:
            pattern = lst[:pattern_length]
            sublists_match = all(
                lst[i:i + pattern_length] == pattern
                for i in range(0, lst_length, pattern_length)
            )
            if sublists_match:
                return pattern
    return None
