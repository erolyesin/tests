from __future__ import print_function
from collections import OrderedDict

numb = int(raw_input())

words = OrderedDict()
for _ in range(numb):
    word = raw_input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words.items()))
for word, count in words.items():
    print("{0}".format(count), end=' ')
