count = 0
for s in open('9-258.txt'):
  data = [int(x) for x in s.split()]
  d3 = [x for x in data if data.count(x) == 3]
  d1 = [x for x in data if data.count(x) == 1]
  if len(d3) == 6 and max(d3) < d1[0]:
    count += 1
print( count )