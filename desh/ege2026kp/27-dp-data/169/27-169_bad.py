with open('27-169a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

count = 0
for i in range(N):
  for j in range(i+1, N):
    s = data[i] + data[j]
    if s >= K:
      count += 1

print( count )

