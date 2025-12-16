def eratos( n ):
  nums = [1]*(n+1)
  for k in range(2, round(n**0.5)+1):
    if nums[k]:
      for m in range(k*k, n+1, k):
        nums[m] = 0
  return [i for i in range(2,n+1) if nums[i]]

primes = eratos( round(10**3.5) )

print( 'Primes ready...' )

def isPrime( n ):
  return n == 2 or \
         all( n % d != 0 for d in range(2, round(n**0.5)+1) )

def split2( n ):
  for d in primes:
    if d > n**0.5: break
    if n % d == 0:
      if isPrime(n//d) and isPrime(d+n//d):
        return d+n//d
  return 0

templates = [ [''] for i in range(3+1) ]
templates[1] = [ f"{i}" for i in range(10) ]
templates[2] = [ f"{i:02}" for i in range(100) ]
templates[3] = [ f"{i:03}" for i in range(1000) ]

res = set()
for nx in range(3):
  for ny in range(3-nx):
    for x in templates[nx]:
      for y in templates[ny]:
        for z in templates[1]:
          n = int( f"12{x}4{y}8{z}" )
          sumPair = split2(n)
          if sumPair:
             res.add( (n, sumPair) )
for r in sorted(res):
  print( *r )

print('---------------------')
a = [12480, 120480, 1200480]
b = [12489, 129489, 1299489]
from fnmatch import fnmatch
for i in range(3):
  for n in range(a[i], b[i]):
    s = str(n)
    sumPair = split2(n)
    if fnmatch(s, '12*4*8?') and sumPair:
      print( n, sumPair )



