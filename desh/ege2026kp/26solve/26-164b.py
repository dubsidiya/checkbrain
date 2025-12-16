with open("26-164.txt") as F:
   data = []
   N, K, M = map(int, F.readline().split())
   for i in range(N):
     size, cost = map(int, F.readline().split())
     data.append( (size, cost) )

data.sort()

dp = [ (size, cost, size) for size, cost in data ] # count, cost, minSize

count = 1
while True:

  found = False
  for i in range(N-1,-1,-1):
    d = data[i]
    valid = [ (size, cost, minSize) for size, cost, minSize in dp[:i]
              if size != 0 and size+K <= d[0] and cost+d[1] <= M ]
    best = min( valid, key = lambda x: (x[1], -x[2]), default = None )
    if best:
      found = True
      dp[i] =  (d[0], best[1]+d[1], best[2])
    else:
      dp[i] = (0, 0, 0)

  if not found: break

  answer = min( (x for x in dp if x != (0,0,0)),
                 key=lambda x: (x[1], -x[2]) )

  print( count )
  count += 1

print( count, answer[1], answer[2] )








