from fnmatch import fnmatch
from math import ceil

def isPrime( n ):
  q = round(n**0.5)
  for d in range(2,q+1):
    if n % d == 0: return False
  return True

mask = '?*37*21'

a = ceil((2*10**8)**0.5)
b = int((3*10**8)**0.5)
qPrimes = [ q for q in range(a,b+1) if isPrime(q) ]
for q in qPrimes:
  n = q*q
  if fnmatch( str(n), mask ):
    print( n, q )

"""
def valid( n ):
  q = round(n**0.5)
  if q*q == n and isPrime(q):
    return q
  else:
    return 0

for n in range(10**8, 2*10**8):
  d = valid( n )
  if d and fnmatch( str(n), mask ):
    print( n, d )
"""