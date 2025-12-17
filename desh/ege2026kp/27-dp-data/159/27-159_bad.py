with open('27-159a.txt') as F:
  N, K = map(int, F.readline().split())
  data = [int(F.readline()) for _ in range(N)]

maxSum = 0
for i in range(0,N):
  if i == 0 or data[i] >= max( data[:i] ):
     for j in range(i+K,N):
        if data[j] >= max( data[:j] ):
          maxSum = max( data[i] + data[j], maxSum )

print( maxSum )

