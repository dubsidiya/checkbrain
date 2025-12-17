with open('27-190a.txt') as F:
  N = int(F.readline())
  data = [int(F.readline()) for _ in range(N)]

maxL = [data[0]] + [0]*(N-1)
for i in range(1,N):
  maxL[i] = max( data[i], maxL[i-1] )

maxR = [0]*(N-1) + [data[-1]]
for k in range(N-2,-1,-1):
  maxR[k] = max( data[k], maxR[k+1] )

maxVal = float('-inf')
for j in range(1,N-1):
  if maxL[j-1] > data[j] and maxR[j+1] > data[j]:
    v = maxL[j-1] - data[j] + maxR[j+1] - data[j]
    if v > maxVal:
      maxVal = v

print( maxVal )
