# Given an array of ints length 3,
# figure out which is larger,
# the first or last element in
# the array, and set all the other
# elements to be that value.
# Return the changed array.
#
#
# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]

def max_end3(arr):

    if arr[0] > arr[-1]:
        arr = [arr[0]] * 3
    else:
        arr = [arr[-1]] * 3
    return arr

    # larger = max(arr[0], arr[-1])
    # arr = [larger] * 3
    # return arr


print(max_end3([4,11,3]))
