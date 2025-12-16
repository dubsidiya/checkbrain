from itertools import permutations

count = 0
for s in open('9.csv'):
  data = list( map(int, s.split(';')) )
  if len(data) == len(set(data)) and \
     any(  2*data[p[0]] == data[p[1]] + data[p[2]] == data[p[3]] + data[p[4]]
           for p in permutations([0, 1, 2, 3, 4]) ):
     count += 1

print( count )

# Вариант 2

count = 0
for s in open('9.csv'):
  data = sorted( map(int, s.split(';')) )
  if len(data) == len(set(data)) and \
     2*data[2] == data[0] + data[4] == data[1] + data[3]:
     count += 1

print( count )