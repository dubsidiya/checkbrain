def isPrime( n ):
  return n > 1 and all( n % d for d in range(2, round(n**0.5)+1) )

def allDivs( n ):
  divs = set()
  for d in range(1, round(n**0.5)+1):
    if n % d == 0:
       divs.add( d )
       divs.add( n//d )
  return sorted(divs)

n = 2_000_000 + 1
count = 0
while count < 6:
  divs = allDivs( n )
  oddDivs = [x for x in divs if x % 2 == 1]
  numOddDivs = len(oddDivs)
  maxPrime = max( x for x in divs if isPrime(x) )
  if numOddDivs == len(divs) and numOddDivs > 30 and numOddDivs % 2 == 1:
    count += 1
    print( n, maxPrime, numOddDivs )
  n += 1
