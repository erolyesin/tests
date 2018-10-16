numb = int(raw_input())
mark_indx = raw_input().split().index('MARKS')

count = sum([float(raw_input().split()[mark_indx]) for _ in range(numb)])

print('%5.2f' % (count/numb))
