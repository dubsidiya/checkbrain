with open('27-177b.txt') as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

def getMaxSum( i, startFrom ):
  if i >= N-1+startFrom: return 0
  return data[i] + max( getMaxSum(i+2, startFrom),
                        getMaxSum(i+3, startFrom) )

print( max( getMaxSum(0, 0), getMaxSum(1, 1) ) )


