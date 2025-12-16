from itertools import product

digits = list('0123456789')
d2 = [ ''.join(dd) for dd in product(digits, repeat=2) ]
d3 = [ ''.join(ddd) for ddd in product(digits, repeat=3) ]

def allDivs( n ):
  q = round(n**0.5)
  divs = [q] if q*q == n else []
  for d in range(1,q):
    if n % d == 0:
      divs.extend( [d, n//d] )
  return sorted(divs)

for s in digits+d2+d3:
  for d in digits:
    n = int( f"3{s}52{d}" )
    divs = allDivs(n)
    if len(divs) % 2 == 1:
      print( n, divs[-2])
