with open('27-189a.txt') as F:
  N = int(F.readline())
  data = [ int(F.readline()) for _ in range(N) ]

maxDiff = float('-inf')
#L0 = M0 = R0 = 0
for L in range(0,N-2):
  for M in range(L+1,N):
    for R in range(M+2,N):
      d = sum(data[M+1:R+1]) - sum(data[L:M+1])
      if d > maxDiff:
        maxDiff = d
        #L0, M0, R0 = L, M, R

#print( L0+1, M0+1, R0+1 )
print( maxDiff )


