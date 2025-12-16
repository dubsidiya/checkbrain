count = 0
for s in open('9-160.csv'):
  data = sorted( map(int, s.split(';')) )
  if data[-1] < sum(data[:-1]) and\
     data[0]+data[-1] == data[1]+data[2]:
    count += 1

print( count )

