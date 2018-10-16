from collections import deque

tests = int(raw_input())

for _ in range(tests):
    raw_input()  # Don't really need this
    sideLengths = deque(map(int, raw_input().split()))

    lastLength = -1
    answer = 'Yes'

    while len(sideLengths) > 0:
        if len(sideLengths) == 1:
            length = sideLengths.pop()
        else:
            if sideLengths[0] < sideLengths[-1]:
                length = sideLengths.pop()
            else:
                length = sideLengths.popleft()

        if lastLength != -1 and length > lastLength:
            answer = 'No'
            break
        else:
            lastLength = length

    print(answer)
