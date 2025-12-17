with open('27-169b.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

Rmax = max(data)
prevRating = [0]*(Rmax + 1)

count = 0
for i in range(N):
  Ri = data[i]
  count += sum( prevRating[K-Ri:] )
  prevRating[Ri] += 1

print( count )
