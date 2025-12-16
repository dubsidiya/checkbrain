def isPrime( n ):
  q = round(n**0.5)
  return n == 2 or \
         (n > 1 and all( n % d != 0 for d in range(2,q+1) ) )

def allPrimeDivs( n ):
  q = round(n**0.5)
  divs = []
  for d in range(2,q+1):
    if n % d == 0:
      divs.extend( [d, n//d] )
  return sorted( divs )

count = 0
n = 6_651_220 + 1
while count < 5:
  divs = allPrimeDivs( n )
  if divs and len(divs) <= 2 and '2' in str(divs[0]) and '2' in str(divs[-1]):
    print( n, divs[-1] )
    count += 1
  n += 1
