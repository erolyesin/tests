#!/bin/python

import math
import os
import random
import re
import sys


# Complete the nonDivisibleSubset function below.

def nonDivisibleSubset(k, S):

    if not k or not len(S):
        return 0

    freq = [0 for _ in range(k)]

    for val in S:
        freq[val % k] += 1

    res = min(freq[0], 1)

    if k % 2 == 0:
        freq[k/2] = min(freq[k/2], 1)

    for count in range(1, k//2 + 1):
        res += max(freq[count], freq[k-count])

    return res

if __name__ == '__main__':

    n = 5

    k = 1

    # S = map(int, "278 576 496 727 410 124 338 149 209 702 282 718 771 575 436".rstrip().split())
    S = map(int, "1 2 3 4 5".rstrip().split())

    result = nonDivisibleSubset(k, S)

    print(str(result) + '\n')

