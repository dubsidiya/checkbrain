with open('27-162a.txt') as F:
  N, K = map(int, F.readline().split() )
  data = []
  for _ in range(N):
    no, val = map( int, F.readline().split() )
    data.append( (no, val) )

maxSum = 0
for i in range(N):
  noi, vali = data[i]
  for j in range(i+K, N):
    noj, valj = data[j]
    if noi == noj and vali+valj > maxSum:
      maxSum = vali + valj

print( maxSum )

