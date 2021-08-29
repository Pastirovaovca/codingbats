# Given an array of ints, return the sum
# of the first 2 elements in the array.
# If the array length is less than 2,
# just sum up the elements that exist,
# returning 0 if the array is length 0.
#
#
# sum2([1, 2, 3]) → 3
# sum2([1, 1]) → 2
# sum2([1, 1, 1, 1]) → 2

def sum2(arr):

    if len(arr) > 2:
        return sum(arr[:2])
    else:
        return sum(arr)

    # if len(arr) >= 2:
    #     return sum((arr[0], arr[1]))
    # elif len(arr) < 2:
    #     return sum(arr[::])



print(sum2([1,2,3]))
