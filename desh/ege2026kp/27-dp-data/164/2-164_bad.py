with open('27-164a.txt') as F:
  N, K = map(int, F.readline().split() )
  data = []
  for _ in range(N):
    no, t, val = map( int, F.readline().split() )
    data.append( (no, t, val) )

data.sort( key = lambda x: x[1])

maxDiff = 0
for i in range(N):
  noi, ti, vali = data[i]
  for j in range(i+1, N):
    noj, tj, valj = data[j]
    if noi == noj and tj - ti >= K and abs(vali-valj) > maxDiff:
      maxDiff = abs(vali - valj)

print( maxDiff )

