with open('27-166a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

maxSum = 0
for i in range(N):
  for j in range(i+K, N):
    for m in range(j+K, N):
      s = data[i] + data[j] + data[m]
      maxSum = max( s, maxSum )

print( maxSum )

