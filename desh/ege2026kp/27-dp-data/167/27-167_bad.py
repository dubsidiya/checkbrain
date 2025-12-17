with open('27-167a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

minProd = float('inf')
for i in range(N):
  for j in range(i+K, N):
    for m in range(j+K, N):
      p = data[i] * data[j] * data[m]
      minProd = min( p, minProd )

print( minProd % (1000000 + 1) )

