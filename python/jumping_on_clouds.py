#!/bin/python

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0
    cloud = 0
    last = len(c) - 1
    while cloud < last:
        jump += 1
        if cloud == last - 1:
            break
        if c[cloud + 2]:
            cloud += 1
        else:
            cloud += 2
    return jump


if __name__ == '__main__':

    c = map(int, "0 0 0 1 0 0".rstrip().split())

    result = jumpingOnClouds(c)

    print(str(result) + '\n')
