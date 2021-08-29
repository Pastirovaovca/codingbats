# Given 2 ints, a and b, return their sum.
# However, sums in the range 10..19 inclusive,
# are forbidden, so in that case just return 20.
#
#
# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21

def sorta_sum(a, b):

    if a + b not in range(10, 20):
        return sum(a, b)
    else:
        return 20

    # num = sum((a, b))
    # if num in range(10, 20):
    #     return 20
    # else:
    #     return num



print(sorta_sum(9,10))
