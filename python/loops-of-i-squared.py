from __future__ import print_function
import itertools

if __name__ == '__main__':
    k, m = 6, 767
    # map(int, raw_input().split())

    lists = []
    for _ in range(k):
        lists.append(map(int, raw_input().split())[1:])

    s = 0
    count = 0
    lcount = 0
    best = []
    smax = 0
    for s_list in itertools.product(*lists):
        s = max(s, sum([x ** 2 for x in s_list]) % m)
        if s > smax:
            smax = s
            best = s_list
        count += len(s_list)
        lcount += 1

    print(s)
    print('lcount: {}'.format(lcount))
    print('count:  {}'.format(count))
    print('best list: ' + str(best))
