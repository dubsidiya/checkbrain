def isPrime( n ):
  return n > 1 and all( n % d != 0 for d in range(2,round(n**0.5)+1) )

def allDivs( n ):
  q = round(n**0.5)
  divs = [] if n % q != 0 else \
         [q] if q == n // q else \
         [q, n//q]
  for d in range(1,q):
    if n % d == 0:
      divs.extend( [d, n//d] )
  return sorted(divs)

def valid( n, divs ):
  s = "".join( map(str, divs) )
  if s.startswith('10') and s.endswith('29'):
    return True
  return False

n = 2352000 + 1
count = 0
while True:
  divs = [ d for d in allDivs(n) if isPrime(d) ]
  if valid( n, divs ):
    print( n, max(divs) )
    count += 1
    if count >= 5: break
  n += 1
