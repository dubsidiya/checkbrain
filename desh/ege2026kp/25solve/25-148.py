def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

def allDivs( x ):
  divs = [1, x]
  d = 2
  while d*d <= x:
    if x % d == 0:
      divs.append( d )
      if x // d > d:
        divs.append( x//d )
    d += 1
  return sorted(divs)

start, end = 113000000, 114000000
from math import ceil, sqrt
for x in range(ceil(sqrt(start//2)), ceil(sqrt(end//2))):
  if isPrime(x):
    n = 2*x*x;
    print( n, x )
    print( allDivs(n) )



