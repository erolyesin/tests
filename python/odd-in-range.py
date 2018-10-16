#!/bin/python

import math
import os
import random
import re
import sys


# Complete the oddNumbers function below.
def oddNumbers(l, r):
    arr = []
    for val in range(l, r):
        if val % 2:
            arr.append(val)
    if r % 2:
        arr.append(r)
    return arr

if __name__ == '__main__':
    print('\n'.join(map(str, oddNumbers(3,9))))
