def repeats(list):
    # Check if the list is None or has less than 2 elements. If so, return None.
    if list is None or len(list) < 2: 
        return None

    # Loop over possible pattern lengths (up to half the length of the list).
    for pattern_length in range(1, len(list) // 2 + 1):
        # Check if the list length is divisible by the pattern length.
        if len(list) % pattern_length == 0:
            # Identify the potential pattern by slicing the list.
            pattern = list[:pattern_length]
            # Check if repeating this pattern forms the original list.
            if pattern * (len(list) // pattern_length) == list:
                # If so, return the pattern.
                return pattern
    
    # If no repeating pattern is found, return None.
    return None

# Test cases
print(repeats(['a', 'b', 1, 'b', 'a', 'b', 1, 'b'])) # Smallest Pattern is = ['a','b','1','b']
print(repeats(['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'])) # Smallest Pattern is = [a,b]
print(repeats(['a', 'b', 'a', 'b', 'a', 'b', 'c'])) # Last element does not have a match = None
print(repeats(['a'])) # One element = None
print(repeats(None)) # None = None
