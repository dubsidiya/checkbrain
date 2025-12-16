def isPrime( n ):
  q = round(n**0.5)
  return n == 2 or \
         (n > 1 and all( n % d != 0 for d in range(2,q+1) ) )

primes = [ x**3 for x in range(2,200) if isPrime(x) ]

def valid( n ):
  i = 0
  while n >= primes[i]:
    d = primes[i]
    if n % d == 0:
      dMax = round(d**(1/3))
      n //= d
    i += 1
  return dMax if n == 1 else 0

count = 0
n = 4_000_000 + 1

while count < 5:
  d = valid( n )
  if d:
    print( n, d )
    count += 1
  n += 1
