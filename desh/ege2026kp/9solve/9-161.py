count = 0
for s in open('9-161.csv'):
  data = sorted( map(int, s.split(';')) )
  doubles = [x for x in data if data.count(x) > 1]
  if data[-1] < sum(data[:-1]) and\
     len(doubles) == 2:
    count += 1

print( count )

