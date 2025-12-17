with open('27-158b.txt') as F:
  N, D, T = map( int, F.readline().split() )
  data = [int(F.readline()) for _ in range(N)]

maxSum = 0
maxND = [0]
for i in range(N):
  if data[i] % D != 0:
    if len(maxND) > T:
      maxSum = max( data[i]+maxND[T], maxSum )
    maxND[0] = max( data[i], maxND[0] )
  else:
    maxND.insert( 0, 0 )

print( maxSum )