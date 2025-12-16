from timeit import default_timer

with open("26-167.txt") as F:
   data = []
   S, N = map(int, F.readline().split())
   for i in range(N):
     size, rank = map(int, F.readline().split())
     data.append( (rank, size) )

"""
S = 40
data = [(5, 5), (5, 5), (5, 5), (3, 4), (3, 5), (1, 2), (20, 36)]
N = len(data)
"""

t0 = default_timer()
data.sort( key = lambda x: x[1] )

dp = [(0, 0)]*(S+1)  # d[totalSize] = (sumRank, maxSize)
for i, d in enumerate(data):
  rank, size = d
  v = { size: max(dp[size], d) }
  for size0 in range(S):
    rank0, _ = dp[size0]
    if rank0:
      newSize = size0 + size
      if newSize <= S:
        v[newSize] = max( dp[newSize], (rank0+rank, size) )
  for size in v:
    dp[size] = max( dp[size], v[size] )

dp = [ (dp[i][0], i, dp[i][1])
        for i in range(S+1) if dp[i] != (0,0) ]

dpSorted = sorted( dp, reverse = True )

print( dpSorted[0] )
print( f"t = {default_timer()-t0}")

