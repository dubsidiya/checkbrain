with open('27-188b.txt') as F:
  N = int(F.readline())
  position = [ int(F.readline()) for i in range(N) ]

position.sort()

data = []
for i in range(N-1):
  data.append( position[i+1] - position[i] )

N = len(data)
INF = float('inf')
dp = [ [INF]*N, [INF]*N ]
dp[1][0] = data[0]

for i in range(1,N):
  dp[0][i] = dp[1][i-1]
  dp[1][i] = data[i] + min( dp[1][i-1], dp[0][i-1] )

print( dp[1][N-1] )



