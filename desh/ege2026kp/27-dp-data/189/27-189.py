with open('27-189b.txt') as F:
  N = int(F.readline())
  data = [ int(F.readline()) for _ in range(N) ]

p = [0]*(N+1)
for i in range(1,N+1):
  p[i] = p[i-1] + data[i-1]

maxpL = [0]*(N+1)
for i in range(N+1):
  maxpL[i] = max( p[i], maxpL[i-1] )

maxpR = [0]*N + [p[-1]]
for i in range(N-1,-1,-1):
  maxpR[i] = max( p[i], maxpR[i+1] )

maxDiff = float('-inf')
for M in range(1,N-2):
  maxRSum = maxpR[M+3] - p[M+1]
  minLSum = p[M+1] - maxpL[M-1]
  d = maxRSum - minLSum
  if d > maxDiff:
    maxDiff = d

print( maxDiff )


