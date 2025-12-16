def alg( s ):
  while any( p in s for p in ['4<', '11<', '00<'] ):
    s = s.replace('11<', '<9', 1)
    s = s.replace('4<', '<5', 1)
    s = s.replace('00<', '<92', 1)
  return s

from math import prod
from itertools import product

pMax = 0
for w in product('014', repeat=10):
  s = alg( ''.join(w) + '<' )
  s = s.replace('<', '')
  p = prod( int(c) for c in s )
  pMax = max( p, pMax )

print( pMax )


