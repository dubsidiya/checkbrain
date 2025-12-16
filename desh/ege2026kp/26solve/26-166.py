with open("26-165.txt") as F:
   data = []
   N, K, Q = map(int, F.readline().split())
   for i in range(N):
     size, cost = map(int, F.readline().split())
     data.append( (cost, size) )

data.sort( key=lambda x: x[1] )

dp = [ (cost, size, size) for cost, size in data ]

for q in range(1,Q):
  for i in range(N-1,-1,-1):
    valid = [(cost, size, minSize)
             for cost, size, minSize in dp
             if size+K <= data[i][1] and cost < float('inf') ]
    if valid:
      prevCost, size, minSize = min( valid, key=lambda x: (x[0],x[2]) )
      dp[i] = (data[i][0]+prevCost, data[i][1], minSize)
    else:
      dp[i] = (float('inf'), 0, 0)

print( min( dp, key=lambda x: (x[0], x[2])) )
