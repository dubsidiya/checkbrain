with open('27-193b.txt') as F:
  N = int(F.readline())
  data = [int(F.readline()) for _ in range(N)]

minLeft = [0]*N
minLeft[0] = data[0]
for i in range(1,N):
  minLeft[i] = min( minLeft[i-1], data[i] )

maxDiffLeft = [0]*N
maxDiffLeft[0] = float('-inf')
for i in range(1,N):
  maxDiffLeft[i] = max( maxDiffLeft[i-1], data[i] - minLeft[i-1] )

maxRight = [0]*N
maxRight[-1] = data[-1]
for i in range(N-2,-1,-1):
  maxRight[i] = max( maxRight[i+1], data[i] )

maxDiffRight = [0]*N
maxDiffRight[-1] = float('-inf')
for i in range(N-2, -1, -1):
  maxDiffRight[i] = max( maxDiffRight[i+1], maxRight[i+1] - data[i] )

sMax = float('-inf')
for i in range(1,N-1):
  sMax = max( maxDiffLeft[i]+maxDiffRight[i+1], sMax )

print( sMax )
