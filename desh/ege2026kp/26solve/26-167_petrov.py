from timeit import default_timer

with open("26-167.txt") as F:
   data = []
   S, N = map(int, F.readline().split())
   for i in range(N):
     size, rank = map(int, F.readline().split())
     data.append( (rank, size) )

"""
S = 40
data = [(5, 5), (5, 5), (5, 5), (4, 3), (5, 3), (2, 1), (36, 20)]
N = len(data)
"""

t0 = default_timer()

data.sort()

dp = { 0: (0, 0) } # totalSize: (sumRank, lastSize)
for rank, size in data:
   v = { size0+size: (dp[size0][0]+rank, size)
             for size0 in dp if size0+size <= S }
   for newSize in v:
     dp[newSize] = max( dp.get(newSize, (0,0)), v[newSize] )

result = max( [(dp[size][0], size, dp[size][1]) for size in dp ] )

print( result )
print( f"t = {default_timer()-t0}" )
