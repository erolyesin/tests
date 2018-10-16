#!/bin/python

import os


# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    remaining = []
    while (len(arr)):
        remaining.append(len(arr))
        cut_size = min(arr)
        arr = [x - cut_size for x in arr if x != cut_size]
    return remaining


if __name__ == '__main__':

    arr = map(int, "5 4 4 2 2 8".split())

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))
