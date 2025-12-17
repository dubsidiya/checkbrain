with open('27-174a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = []
  for i in range(N):
    pos, count = map( int, F.readline().split() )
    data.append( [pos, count] )

#print( data )

totals = []
for pos, count in data:
  dataSorted = sorted( data, key = lambda d: abs(d[0]-pos) )
  i, remains, s = 1, max(0, K-dataSorted[0][1]+1), 0
  while remains:
    dist = abs(dataSorted[i][0] - pos)
    Ki = min( remains, dataSorted[i][1] )
    remains -= Ki
    s += Ki*dist
    i += 1
  totals.append( (s, pos) )

totals.sort()
totals = [ d for d in totals if d[0] == totals[0][0] ]
if len(totals) == 1:
  print( totals[0][1] )
else:
  print( totals[-1][1] - totals[0][1] )




