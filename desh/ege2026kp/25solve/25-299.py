def matchMask( s ):
  if not (s.startswith('78') and s.endswith('321') ):
    return False
  s = s[2:-3]
  if '56' not in s: return False
  pos = s.index('56')
  return all( c in '13579' for c in s[pos+2:] ) and \
         len(s[:pos]) == 1

from math import ceil
D = 279
start = ceil( 78056321/D ) * D
for n in range(start, 79000000000, D):
  if n % D == 0 and matchMask( str(n) ):
     print( n, n // D )
