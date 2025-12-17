with open('27-181b.txt') as F:
  N = int(F.readline())
  A = [ int(F.readline()) for _ in range(N) ]
  B = [ int(F.readline()) for _ in range(N) ]

minDiff = 10**10

j = 0
for i in range(N):
  while j < N and B[j] < A[i]:
    minDiff = min( abs(A[i] - B[j]), minDiff )
    j += 1
  if j < N:
    minDiff = min( abs(A[i] - B[j]), minDiff )

print( minDiff )