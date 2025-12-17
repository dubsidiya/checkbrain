with open('27-171a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

D = 111

count = 0
for i in range(N):
  s = 0
  for j in range(i, N):
    s += data[j]
    if j - i + 1 >= K and s % D == 0:
      # print( i, j )
      count += 1

print( count )
