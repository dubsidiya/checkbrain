from math import ceil
from fnmatch import fnmatch

def isPrime( n ):
  return n == 2 or all( n % d for d in range(2, round(n**0.5)+1) )

start = ceil( 1020201**0.5 )
end = int( 1929999291**0.5 )

for q in range(start, end+1):
  x = q**2
  if fnmatch( str(x), "1?2*0*2?1" ) and isPrime(q):
    print( x, q )
