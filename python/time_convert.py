#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    oldhour = int(s[0:2])
    if "PM" in s and oldhour != 12:
        oldhour = int(s[0:2])
        newhour = (oldhour + 12) % 24
        s = s.replace("%02d" % oldhour, "%02d" % newhour, 1)
        print("%02d -> %02d" % (oldhour, newhour))
    elif "AM" in s and oldhour == 12:
        s = s.replace("12", "00", 1)

    s = s.replace("AM", "").replace("PM", "")
    return s


if __name__ == '__main__':

    s = "12:34:54AM"

    result = timeConversion(s)

    print(result + '\n')

