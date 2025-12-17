with open('27-168a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

maxProd = 0
for i in range(N):
  for j in range(i+K, N):
    for m in range(j+K, N):
      s = data[i] * data[j] * data[m]
      maxProd = max( s, maxProd )

print( maxProd % (10**6 + 1))

