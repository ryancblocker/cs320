def extract(list_s, lo, hi):
    
    def bound(list_s, target, isLow):
        left = 0
        right = len(list_s)

        while left < right:
            mid = (left + right) // 2
            if list_s[mid] < target or (isLow and list_s[mid] == target):
                left = mid + 1
            else:
                right = mid  #found lo bound
        return left

    # def hi_bound(list_s, target):
    #     left = 0
    #     right = len(list_s)

    #     while left < right:
    #         mid = (left + right) // 2
    #         if list_s[mid] <= target:
    #             left = mid + 1
    #         else:
    #             right = mid  #found lo bound
    #     return left

    if list_s is None:
        return None
    
    elif len(list_s) is 0:
        return list_s
    
    elif lo is None:
        return list_s[0:hi]

    elif hi is None:
        return list_s[bound(list_s, lo-1, isLow=True):]

    elif lo and hi is None:
        return list_s
    
    elif lo > hi:
        return None
    
    lo = bound(list_s, lo, isLow=True)
    hi = bound(list_s, hi, isLow=False)

    return list_s[lo:hi]

print(extract(None, 1, 5)) # Should print None
print(extract([], 1, 5)) # Should print []
print(extract([1, 2, 3, 4, 5], 5, 1)) # Should print None
print(extract([1, 2, 3, 4, 5], None, 3)) # Should print [1, 2, 3]
print(extract([1, 2, 3, 4, 5], 3, None)) # Should print [3, 4, 5]
print(extract([2, 2, 3, 4, 4, 5], 2, 4)) # Should print [2, 2, 3, 4, 4]
print(extract([1, 3, 5, 7, 9], 4, 8)) # Should print [5, 7]
print(extract([1, 2, 3, 4, 5], 0, 6)) # Should print [1, 2, 3, 4, 5]