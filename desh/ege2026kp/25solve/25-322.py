from fnmatch import fnmatch

def isPrime( n ):
  return n >= 2 and \
         all( n % d != 0 for d in range(2,round(n**0.5)+1) )

def sumDigits( n ):
  return sum( map(int, str(n)) )

D = 2423
mask = '3*51?5*7'

for n in range(0, 4*10**8, D):
  if fnmatch( str(n), mask ):
    if isPrime(sumDigits(n)):
      print( n, n // D )
