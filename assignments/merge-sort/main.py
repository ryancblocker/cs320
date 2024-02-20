def mergesort(mlist):

    if mlist is None:
        return None
    if not isinstance(mlist, list):
        return None
    if len(mlist) == 0:
        return []
    
    if (len(mlist) > 1):
        mid = len(mlist) // 2
        right_side = mlist[mid:]
        left_side = mlist[:mid]
        
        mergesort(right_side)
        mergesort(left_side)

        right_index = left_index = mlist_index = 0

        while (left_index < len(left_side) and right_index < len(right_side)):
            if right_side[right_index] <= left_side[left_index]:
                mlist[mlist_index] = right_side[right_index]
                right_index += 1
            else:
                mlist[mlist_index] = left_side[left_index]
                left_index += 1
            mlist_index += 1

        while right_index < len(right_side):
            mlist[mlist_index] = right_side[right_index]
            right_index += 1
            mlist_index += 1

        while left_index < len(left_side):
            mlist[mlist_index] = left_side[left_index]
            left_index += 1
            mlist_index += 1
        
    return mlist
