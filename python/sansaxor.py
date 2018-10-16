#!/bin/python

from __future__ import division

# samples:
# 98, 74, 12 -> 110
# 50, 13, 2 -> 48

# 1, 2, 3 -> 1,2,3,1x2,2x3,1x2x3 -> 2
# 4, 5, 7, 5 -> 4,5,7,5,4x5,5x7,7x5,4x5x7,5x7x5,4x5x7x5 -> 0

# 12, 23, 34, 45, 56 ->

# 12, 23, 34, 45, 56, 12x23, 23x34, 34x45, 45x56,
# 12x23x34, 23x34x45, 34x45x56,
# 12x23x34x45, 23x34x45x56, 12x23x34x45x56 ->

# (12x12x12x12x12)x(23x23x23x23x23x23x23x23)x
# (34x34x34x34x34x34x34x34x34)x(45x45x45x45x45x45x45x45)x
# (56x56x56x56x56) ->
# (0x12)x(0)x(0x34)x(0)x(0x56)

# Self XORing any number with itself even number of times results in zero.
# And, XORing any number with itself odd number of times results in itself.
# So, any array of even size will always result in zero
# Odd sized array only needs to XOR the array once for those numbers that appear odd number of times.
# And, it appears that for odd sized arrays the even indexed numbers appear odd number of times.


def sansaXor(arr):
    if not len(arr) % 2:
        return 0

    xor_vals = 0
    for indx, val in enumerate(arr):
        if not indx % 2:
            xor_vals ^= val

    return xor_vals


if __name__ == '__main__':

    arrs = [[98, 74, 12], [50, 13, 2], [1, 2, 3], [4, 5, 7, 5], [12, 23, 34, 45, 56]]

    for arr in arrs:

        result = sansaXor(arr)

        print(str(result) + '\n')
