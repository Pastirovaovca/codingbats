# Given 3 int values, a b c, return their sum.
# However, if one of the values is 13 then it
# does not count towards the sum and values to
# its right do not count. So for example,
# if b is 13, then both b and c do not count.
#
#
# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):

    z = [a, b, c]

    if 13 in z:
        return sum(z[:z.index(13)])
    else:
        return sum(z)

    # nums = (a, b, c)
    # added = []
    # for item in nums:
    #     if item == 13:
    #         break
    #     else:
    #         added.append(item)
    # return sum(added)

print(lucky_sum(13,13,3))
