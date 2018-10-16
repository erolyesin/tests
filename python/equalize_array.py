#!/bin/python

import math
import os
import random
import re
import sys


# Complete the equalizeArray function below.
def equalizeArray(arr):
    mode_val = max(set(arr), key=arr.count)

    count = len(arr) - arr.count(mode_val)

    return count

if __name__ == '__main__':
    arr = map(int, "3 3 2 1 3".rstrip().split())

    result = equalizeArray(arr)

    print(str(result) + '\n')
