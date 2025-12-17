with open("27-182b.txt") as F:
  N, K = map( int, F.readline().split() )
  data = [int(x) for x in F]

sMax = float('-inf')
maxK = float('-inf')
for i in range(K,N):
  maxK = max( data[i-K], maxK )
  sMax = max( maxK + data[i], sMax )

print( sMax )
