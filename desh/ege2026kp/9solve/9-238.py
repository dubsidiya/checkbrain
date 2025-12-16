data = [ [] for i in range(6) ]
for s in open('9-228.txt'):
  d = list( map(int, s.split()) )
  for i in range(6):
    data[i].append( d[i] )

count = 0
for i in range(len(data[0])):
  row = [ col[i] for col in data ]
  for i, x in enumerate(row):
    if row.count(x) == 1 and data[i].count(x) > 180:
      count += 1

print( count )

