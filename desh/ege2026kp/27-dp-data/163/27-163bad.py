with open('27-163a.txt') as F:
  N, K = map(int, F.readline().split() )
  data = []
  for _ in range(N):
    no, val = map( int, F.readline().split() )
    data.append( (no, val) )

maxDiff = 0
for i in range(N):
  noi, vali = data[i]
  for j in range(i+K, N):
    noj, valj = data[j]
    if noi == noj and abs(vali-valj) > maxDiff:
      maxDiff = abs(vali - valj)

print( maxDiff )

