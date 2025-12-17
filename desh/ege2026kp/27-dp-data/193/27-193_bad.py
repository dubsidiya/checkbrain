with open('27-193a.txt') as F:
  N = int(F.readline())
  data = [int(F.readline()) for _ in range(N)]

sMax = float('-inf')
for i in range(N):
 for j in range(i+1, N):
  for k in range(j+1,N):
   for m in range(k+1,N):
     sMax = max( data[j] - data[i] + data[m] - data[k], sMax )

print( sMax )

