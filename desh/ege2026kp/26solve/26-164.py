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
    best = None
    for j in range(i):
      x = dp[count-1][j]
      if x != (0,0,0) and x[0]+K <= d[0] and x[1]+d[1] <= M and \
         (best is None or x[1] < best[1] or x[1] == best[1] and x[2] > best[2]):
         best = x
         found = True
    if best:
      dp[count][i] =  [d[0], best[1]+d[1], best[2]]

  if not found:
    dp.pop()
    break

  print( count )
  count += 1

candidates = sorted( (x for x in dp[-1] if x != (0,0,0)),
                     key=lambda x: (x[1], -x[2]) )

print( count, candidates[0][1], candidates[0][2] )








