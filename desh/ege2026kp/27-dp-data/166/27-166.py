with open('27-166b.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

max1 = max2 = max3 = 0
for i in range(2*K,N):
  max1 = max( data[i-2*K], max1 )
  max2 = max( max1+data[i-K], max2 )
  max3 = max( max2+data[i], max3 )

print( max3 )

