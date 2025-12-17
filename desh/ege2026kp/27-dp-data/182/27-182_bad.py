with open("27-182a.txt") as F:
  N, K = map( int, F.readline().split() )
  data = [int(x) for x in F]

sMax = float('-inf')
for i in range(N):
  for j in range(i+K,N):
    s = data[i] + data[j]
    if s > sMax:  sMax = s

print( sMax )
