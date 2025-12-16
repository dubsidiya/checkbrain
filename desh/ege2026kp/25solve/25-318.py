
D = 2023

x = 10**9
while x % D != 0:
  x += 1

res = []
maxSum = 0
for n in range( x, 2*10**9, D ):
  if n % 10 == 1:
    s = str(n)
    sumDig = sum( map( int, s ) )
    if sumDig > maxSum:
      maxSum = sumDig
      res = [n]
    elif sumDig == maxSum:
      res.append( n )

res.sort( reverse = True )

for n in res:
  print( n, n//D )



