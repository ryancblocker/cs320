# def repeats(lst):
    # check if list is None
    # check if input is not a list
    # check if list has less thn two elements

    #set lst length

    #for every pattern length in half of the list length going backwards
        #if the pattern length is divisible by the list
            #then set the pattern size equal to the remainder of the list
            #if the entire list is made up of repetitions of the pattern.
                #return it (pattern found) ;)
    #return pattern not found

def repeats(lst):
    if lst is None or not isinstance(lst, list):
        raise None

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


# Test cases
print(repeats(['a', 'b', 1, 'b', 'a', 'b', 1, 'b']))  #['a', 'b', 1, 'b']
print(repeats(['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']))  #['a','b','a','b']
print(repeats(['a', 'b', 'a', 'b', 'a', 'b']))  #['a', 'b']
print(repeats(['a', 'b', 'a', 'b', 'a', 'b', 'c']))  #None
print(repeats([1]))  #None