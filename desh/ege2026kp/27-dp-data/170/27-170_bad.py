with open('27-170a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

maxSum = float('-inf')
for i in range(N):
  s = 0
  for j in range(i, N):
    s += data[j]
    if j - i >= K:
      maxSum = max( s, maxSum )

print( maxSum )
