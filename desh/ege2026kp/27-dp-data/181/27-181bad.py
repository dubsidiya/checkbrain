with open('27-181a.txt') as F:
  N = int(F.readline())
  A = [ int(F.readline()) for _ in range(N) ]
  B = [ int(F.readline()) for _ in range(N) ]

minDiff = 10**10
for i in range(N):
  for j in range(N):
    minDiff = min( abs(A[i] - B[j]), minDiff )

print( minDiff )