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
    if lst is None or len(lst) < 2:
        return None

    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    lst_length = len(lst)
    for pattern_length in range(lst_length // 2, 0, -1):
        if lst_length % pattern_length == 0:
            pattern = lst[:pattern_length]
            if all(lst[i:i + pattern_length] == pattern for i in range(0, lst_length, pattern_length)):
                return pattern
    return None

def check_test_case(test_function, test_input, expected_output):
    actual_output = test_function(test_input)
    return actual_output == expected_output, actual_output

# Test cases
test_cases = [
    (['a', 'b', 'c', 'd'], None),
    (['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'], ['a', 'b','a','b']),
    (['c', 'a', 'b', 'c', 'a', 'b'], ['c', 'a', 'b']),
    (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g'], ['a', 'b', 'c', 'd', 'e', 'f', 'g']),
    (None, None)
]

all_correct = True
wrong_outputs = []

for test_input, expected_output in test_cases:
    is_correct, actual_output = check_test_case(repeats, test_input, expected_output)
    if not is_correct:
        all_correct = False
        wrong_outputs.append(f"Input: {test_input}, Expected: {expected_output}, Got: {actual_output}")

if all_correct:
    print("Correct")
else:
    print("Wrong")
    for wrong_output in wrong_outputs:
        print(wrong_output)



