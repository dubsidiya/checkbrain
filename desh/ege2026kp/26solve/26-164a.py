with open("26-164.txt") as F:
   data = []
   N, K, M = map(int, F.readline().split())
   for i in range(N):
     size, cost = map(int, F.readline().split())
     data.append( (size, cost) )

data.sort()

dp = [ [(size, cost, size) for size, cost in data] ] # count, cost, minSize

count = 1
while True:
  dp.append( [(0, 0, 0)]*N )

  found = False
  for i in range(N):
    d = data[i]
    valid = [ (size, cost, minSize) for size, cost, minSize in dp[count-1]
              if size != 0 and size+K <= d[0] and cost+d[1] <= M ]
    best = min( valid, key = lambda x: (x[1], -x[2]), default = None )
    if best:
      found = True
      dp[count][i] =  [d[0], best[1]+d[1], best[2]]

  if not found:
    dp.pop()
    break

  print( count )
  count += 1

candidates = sorted( (x for x in dp[-1] if x != (0,0,0)),
                     key=lambda x: (x[1], -x[2]) )

print( count, candidates[0][1], candidates[0][2] )








