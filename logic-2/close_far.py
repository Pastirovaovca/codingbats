# Given three ints, a b c, return True if
# one of b or c is "close" (differing from
# a by at most 1), while the other is "far",
# differing from both other values by 2 or
# more. Note: abs(num) computes the absolute
# value of a number.
#
#
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True

def close_far(a, b, c):

    if abs(a - b) <= 1 and min(a, b) - 2 >= c or max(a, b) + 2 <= c:
        return True
    elif abs(a - c) <= 1 and min(a, c) - 2 >= b or max(a, c) + 2 <= b:
        return True
    else:
        return False


print(close_far(10,9,6))
