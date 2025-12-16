from fnmatch import fnmatch

def isPrime( n ):
  return n == 2 or \
         all( n % d != 0 for d in range(2, round(n**0.5)+1) )

D = 4019
for n in range(0, 1935999990, D):
  s = str(n)
  sd = sum( map(int, s) )
  if fnmatch(s, '1?359*0') and isPrime(sd):
    print( n, n // D )

