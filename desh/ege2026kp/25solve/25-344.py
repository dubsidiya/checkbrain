from fnmatch import fnmatch
from math import ceil

def isPrime( n ):
  q = round(n**0.5)
  for d in range(2,q+1):
    if n % d == 0: return False
  return True

mask = '?*23*21'

a = ceil((10**9)**0.25)
b = int((10**10)**0.25)
qPrimes = [ q for q in range(a,b+1) if isPrime(q) ]
for q in qPrimes:
  n = q**4
  if fnmatch( str(n), mask ):
    print( n, q*q )
