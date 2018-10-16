from collections import OrderedDict

numb = int(raw_input())

items = OrderedDict()
for _ in range(numb):
    item = raw_input().rsplit(' ', 1)
    if item[0] in items:
        items[item[0]] += int(item[1])
    else:
        items[item[0]] = int(item[1])

for item, price in items.items():
    print("{0} {1}".format(item, price))
