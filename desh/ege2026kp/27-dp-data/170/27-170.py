with open('27-170b.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

maxSum = float('-inf')
minPrevSumK = float('inf')
totalSum = totalSumK = 0
for i in range(N):
  totalSum += data[i]
  if i >= K:
    minPrevSumK = min( totalSumK, minPrevSumK )
    maxSum = max( totalSum - minPrevSumK, maxSum )
    totalSumK += data[i-K]

print( maxSum )
