#pseudo code
# The Big Oh of this should be O(k log k)

#extract declaration (list, low, high)
    #if list is None
        #return None

    #if low > high
        #return None

    #if low or high = None
        #return all values

    #if list is empty
        #return the elements in empty list

    #if low and high are not given
        #return all values

#test with [2,2,3,4] 2 and 4
#test with []
#test with [1,2,3,4,5,6,7,8,9] 4 and 9
#test with []


def extract(list_s, lo, hi):
    return 0