with open('27-165b.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

min1 = min2 = min3 = 10**10
for i in range(2*K,N):
  min1 = min( data[i-2*K], min1 )
  min2 = min( min1+data[i-K], min2 )
  min3 = min( min2+data[i], min3 )

print( min3 )

