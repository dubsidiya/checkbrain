def isPrime( n ):
  return n > 1 and all( n % d for d in range(2, round(n**0.5)+1) )

def allDivs( n ):
  divs = set()
  for d in range(1, round(n**0.5)+1):
    if n % d == 0:
       divs.add( d )
       divs.add( n//d )
  return sorted(divs)

count = 0
n = 100000000 + 1
while count < 5:
  divs = allDivs( n )
  primeDivs = [d for d in divs if isPrime(d)]
  evenDivs = [d for d in divs if d % 2 == 0]
  if len(primeDivs) == len(evenDivs):
    print( n, abs( sum(primeDivs) - sum(evenDivs) ) )
    count += 1
  n += 1