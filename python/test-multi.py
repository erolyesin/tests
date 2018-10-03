# !/usr/bin/env python

__author__ = 'erol'

"""
sandbox file
"""

## 1. create a method given an integer
# returns the number of set bits
def count_bits(var):
    count = 0
    val = int(var)
    while (val):
        val &= (val - 1)
        count += 1
        print "[%d] : val = %d|%d : count = %d" % ( var, val, val-1, count)
    return count

## 3. create a method that swaps values of two integers without introducing more memory space
def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b

## 4. create a method where given the hour and minute
# returns the angle between the two hands
def time_angle(hour, minute):

    hour %= 12
    minute %= 60

    hr_angle = (30*hour + 0.5*minute)
    mn_angle = 6*minute

    angle = 30*hour + 5.5*minute

    angle = abs(hr_angle - mn_angle)

    print "hr_angle = %d" % hr_angle
    print "mn_angle = %d" % mn_angle
    print "angle = %d" % angle

    if angle > 180:
        angle = 360 - angle
        print "angle = %d" % angle

    return  angle

## 5. method signature for variable arguments involving tupiles and dictionaries
def foo(*args, **kargs):
    print 'args:', args
    print 'kargs:', kargs

if __name__ == '__main__':

    val1 = 10
    val2 = 10

    ## 2. what will be the output
    lst = [val1, val2]
    print lst[1:]

    foo(val1, val2, a=val1, b=val2)

    val1, val2 = swap(val1, val2)

    foo(val1, val2, a=val1, b=val2)

    print 'val2 = %d; %d bits' % (val2, count_bits(val2))
    print 'val1 = %d; %d bits' % (val1, count_bits(val1))

    print 'time: ' + str(min(val1, val2)%12) + ":" + str(max(val1, val2)%60)
    print time_angle( hour=min(val1, val2), minute=max(val1, val2)), 'degress'
