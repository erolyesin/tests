#!/bin/python
from __future__ import print_function

def ashtonString(str, chr_offset):
    """
    "set" data structure in python has a large RAM footprint and returns a MemoryError in case of very long string. Due to this, the solution can only pass
    through the first 4 testcases. Any other solutions are welcome. :)
    """
    arr = []
    end = 1
    while end != len(str):
        for bgn in range(len(str) - end + 1):
            arr.append(str[bgn:bgn + end])
        end += 1
    arr.sort()
    arr = ''.join(arr)
    print(arr)
    return arr[chr_offset - 1]


if __name__ == '__main__':

    s = 'edvidhafc'

    k = 3

    res = ashtonString(s, k)

    print(res + '\n')
