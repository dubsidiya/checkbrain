with open("26-160.txt") as F:
   data = []
   N = int(F.readline())
   for i in range(N):
     t0, t1, cost = map(int, F.readline().split())
     data.append( (t0, t1, t1-t0+1, cost) )

"""
N = 3
data = [
[10, 90, 81, 1],
[100, 130, 31, 2],
[120, 135, 16, 5],
[130, 170, 41, 3],
[140, 180, 41, 4],
]
"""

data.sort( key = lambda x: x[1] )

dp = [ data[i][2] for i in range(N) ]

for i in range(1,N):
  dp[i] = dp[i] + max( (dp[j] for j in range(i)
                        if data[j][1] < data[i][0]), default= 0 )
maxTotalTime = max(dp)

count = 0
totalCost = 0
R = maxTotalTime
i = dp.index(maxTotalTime)
while True:
  print( i, end = " ")
  totalCost += data[i][3]
  count += 1
  R -= data[i][2]
  if not R: break
  indices = [ k for k in range(i)
              if dp[k] == R and dp[k] + data[i][2] == dp[i] and
                 data[k][1] < data[i][0] ]
  #if len(indices) > 1:
  #  print( indices )
  i = indices[0]

print()
print( maxTotalTime, totalCost, count )

print('------------------------------------')

# На основе решения А. Богданова

dp = [] # maxTime, cost, count, tEnd

for t0, t1, dt, cost in data:
   best = max( ( v for *v, tEnd in dp if t0 > tEnd ),
                 default=[0, 0, 0, -1]  )
   dp.append( [best[0]+dt, best[1]+cost, best[2]+1, t1] )

print( *max(dp)[:3] )







