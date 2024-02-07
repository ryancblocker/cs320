def extract(list_s, lo, hi):
    
    def lo_bound(list_s, target):
        left = 0
        right = len(list_s)

        while left < right:
            mid = (left + right) // 2
            if list_s[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def hi_bound(list_s, target):
        left = 0
        right = len(list_s)

        while left < right:
            mid = (left + right) // 2
            if list_s[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    if list_s is None:
        return None
    
    elif len(list_s) is 0:
        return list_s
    
    elif lo is None:
        return list_s[0:hi]

    elif hi is None:
        return list_s[lo_bound(list_s, lo):len(list_s)]

    elif lo and hi is None:
        return list_s
    
    elif lo > hi:
        return None
    
    lo = lo_bound(list_s, lo)
    hi = hi_bound(list_s, hi)

    return list_s[lo:hi]
