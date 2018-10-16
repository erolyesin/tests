#!/bin/python

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    s_len = len(s)
    mult = n / s_len
    addn = n % s_len
    count = 0
    for char in s[:n]:
        if 'a' in char:
            count += 1
    count *= mult
    for char in s[:addn]:
        if 'a' in char:
            count += 1
    return count


if __name__ == '__main__':
    s = "aba"

    n = 9

    result = repeatedString(s, n)

    print(str(result) + '\n')
