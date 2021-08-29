# Given an int array length 2,
# return True if it contains a 2 or a 3.
#
#
# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has23(arr):

    if 2 in arr or 3 in arr:
        return True
    return False
    
    # if arr.count(2) or arr.count(3):
    #     return True
    # return False

print(has23([1,4]))
