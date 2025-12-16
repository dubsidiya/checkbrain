def allPrimes( n ):
  primes = set(range(2,n+1))
  q = round(n**0.5)
  for k in range(2,q+1):
    if k in primes:
      for i in range(k*k,n+1,k):
        if i in primes:
          primes.remove(i)
        i += k
  return primes

end = 10**11
primes = allPrimes( int((10**11)**0.5) )

for i in primes:
  for k in primes:
    if k > 2:
      n = i**(k-1)
      if n > end: break
      if n % 10 != 1 and '2025' in str(n):
        print( n, n//i )

