with open('27-181b.txt') as F:
  N = int(F.readline())
  A = [ int(F.readline()) for _ in range(N) ]
  B = [ int(F.readline()) for _ in range(N) ]

N //= 32

with open('27-181bd.txt', "w") as F:
  print( N, file=F )
  for i in range(N):
    print( A[i], file=F )
  for i in range(N):
    print( B[i], file=F )
