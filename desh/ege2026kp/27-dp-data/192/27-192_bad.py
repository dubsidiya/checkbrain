import timeit

with open('27-192a.txt') as F:
  N = int(F.readline())
  data = [int(F.readline()) for _ in range(N)]

t0 =  timeit.default_timer()
sMax = float('-inf')
for L in range(N):
 for Q in range(L+1, N):
  for R in range(Q+2,N):
   for T in range(R+1,N):
     sMax = max( sum(data[L:Q+1]) + sum(data[R:T+1]), sMax )

print( sMax, timeit.default_timer()-t0 )

t0 =  timeit.default_timer()
sMax = float('-inf')
for L in range(N):
 SLQ = data[L]
 for Q in range(L+1, N):
  SLQ += data[Q]
  for R in range(Q+2,N):
   SRT = data[R]
   for T in range(R+1,N):
     SRT += data[T]
     sMax = max( SLQ + SRT, sMax )

print( sMax, timeit.default_timer()-t0 )
