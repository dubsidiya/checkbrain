with open('27-192b.txt') as F:
  N = int(F.readline())
  data = [int(F.readline()) for _ in range(N)]

maxSumLeft = [0]*N
maxSumLeft[0] = data[0]
maxSumLeft[1] = data[0]+data[1]
for i in range(2,N):
  maxSumLeft[i] = max( maxSumLeft[i-1]+data[i],
                       data[i]+data[i-1] )
for i in range(2,N):
  maxSumLeft[i] = max( maxSumLeft[i-1], maxSumLeft[i] )

maxSumRight = [0]*N
maxSumRight[-1] = data[-1]
maxSumRight[-2] = data[-2] + data[-1]
for i in range(N-3,-1,-1):
  maxSumRight[i] = max( maxSumRight[i+1]+data[i],
                        data[i]+data[i+1] )
for i in range(N-3,-1,-1):
  maxSumRight[i] = max( maxSumRight[i+1], maxSumRight[i] )

sMax = float('-inf')
for i in range(2, N-2):
  sMax = max( maxSumLeft[i-1]+maxSumRight[i+1], sMax )

print( sMax )