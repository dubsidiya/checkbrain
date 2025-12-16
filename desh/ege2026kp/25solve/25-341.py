from fnmatch import fnmatch
from math import ceil

def isPrime( n ):
  q = round(n**0.5)
  for d in range(2,q+1):
    if n % d == 0: return False
  return True

mask = '?*26*89'

a = ceil((3*10**8)**0.5)
b = int((6*10**8)**0.5)
qPrimes = [ q for q in range(a,b+1) if isPrime(q) ]
for q in qPrimes:
  n = q*q
  if fnmatch( str(n), mask ):
    print( n, q )
