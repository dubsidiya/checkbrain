def allDivs( n ):
    divs = set()
    for d in range(1,round(n**0.5)+1):
       if n % d == 0:
          divs.add( d )
          divs.add( n // d )
    return sorted(list(divs))

def isPrime( n ):
   return n > 1 and all( n % d != 0 for d in range(2,round(n**0.5)+1) )

def valid( n ):
   divs = [ d for d in allDivs(n) if isPrime(d) ]
   if len(divs) <= 3: return False, 0
   q = divs[1] - divs[0]
   for a, b in zip(divs, divs[1:]):
      if b - a != q: return False, 0
   return True, q*len(divs)

start, end = 100000, 500000
for n in range(start, end+1):
  OK, M = valid( n )
  if OK:
     print( n, M)
