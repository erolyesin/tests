#!/bin/python
import string

#
# Complete the 'checkIPs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY ip_array as parameter.
#

def checkIPs(ip_array):
    ret = []
    for addr in ip_array:
        if '.' in addr:
            arr = addr.split('.')
            if len(arr) != 4:
                ret.append('Neither')
                break
            for group in arr:
                if not group.isdigit() or int(group) < 0 or int(group) >255:
                    ret.append('Neither')
                    break
            else:
                ret.append('IPv4')
        elif ':' in addr:
            arr = addr.split(':')
            for group in arr:
                if all(c not in string.hexdigits for c in group) and group != '':
                    ret.append('Neither')
                    break
                if len(arr) > 8 or (group.isalnum() and int(group, 16) > 2 ** 128):
                    ret.append('Neither')
                    break
            else:
                ret.append('IPv6')
        else:
            ret.append('Neither')
    return ret

if __name__ == '__main__':
    ip_array_count = int(raw_input().strip())

    ip_array = []

    for _ in xrange(ip_array_count):
        ip_array_item = raw_input()
        ip_array.append(ip_array_item)

    result = checkIPs(ip_array)

    print('\n'.join(result))
    print('\n')
