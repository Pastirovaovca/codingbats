# Given an array of ints, return True if
# one of the first 4 elements in the array
# is a 9. The array length may be less than 4.
#
#
# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

def array_front9(arr):

    # for i in range(len(arr[:4])):
    #     if arr[i] == 9:
    #         return True
    # return False

    if 9 in arr[:4]:
        return True
    return False


print(array_front9([1, 1, 1, 2, 9]))
