with open('27-165a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

minSum = 10**10
for i in range(N):
  for j in range(i+K, N):
    for m in range(j+K, N):
      s = data[i] + data[j] + data[m]
      minSum = min( s, minSum )

print( minSum )

