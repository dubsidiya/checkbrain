def isPrime( n ):
  return n > 0 and (n == 2 or \
         all( n % d != 0 for d in range(2,round(n**0.5)+1) ) )

primes = [ n for n in range(6*9+1) if isPrime(n) ]

primeSum = set()
for n in range(10**6):
  s = str(n)
  p = sum( map(int, s) )
  if isPrime(p):
    for k in range(0,7-len(s)):
      primeSum.add( '0'*k + s )

result = {}
for s in primeSum:
  n = int( f"1234{s}" )
  p = sum( map(int, s) )
  if n % (p+2)**3 == 0:
    if p not in result or n < result[p]:
      result[p] = n

result = sorted( result.items(), key = lambda x: x[1]  )
for r in result:
  print( r[1], r[0])
