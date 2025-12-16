def allPrimes( n ):
  primes = [1]*(n+1)
  p = 2
  while p*p <= n:
    for k in range(2*p,n+1,p):
      primes[k] = 0
    p += 1
    while p*p <= n and not primes[p]:
      p += 1
  return set( i for i in range(2,n+1) if primes[i] )

primes = allPrimes( 10**5 )

for n in range( 900, 10**7-1 ):
  s = str(n)
  if s[0] != '9': continue
  p = s[1:-1]
  if int(p) in primes and  n % 9998 == 0:
    print( n, n // 9998 )