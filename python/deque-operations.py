from __future__ import print_function
from collections import deque

d = deque()

d_dict = {'append':d.append, 'pop':d.pop, 'popleft':d.popleft, 'appendleft':d.appendleft}

numb = int(raw_input())

for _ in range(numb):
    command = raw_input().split()
    if 'pop' in command[0]:
        d_dict[command[0]]()
    else:
        d_dict[command[0]](command[1])

print(*list(d))