with open('27-180b.txt') as F:
  N = int(F.readline())
  data = [ int(s) for s in F ]

N //= 63

with open('27-180bd.txt', "w") as F:
  print( N, file=F )
  for i in range(N):
    print( data[i], file=F )
