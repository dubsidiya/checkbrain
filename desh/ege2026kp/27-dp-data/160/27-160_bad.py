with open('27-160a.txt') as F:
  N = int(F.readline())
  data = [int(F.readline()) for _ in range(N)]

totalSum = sum(data)
maxSum = 0
for i in range(N-1):
  for j in range(i+1, N):
    sum1 = sum(data[i:j+1])
    s1 = data[i] + data[j]
    sum2 = totalSum - sum1
    s2 = data[i-1] + data[(j+1)%N]
    if j+1-i >= 2 and j+1-i <= N-2 and \
       sum1 % s1 == 0 and sum2 % s2 == 0:
       if s1 + s2 > maxSum:
         print( i, j, sum1, sum2 )
       maxSum = max( s1+s2, maxSum )

print( maxSum )


