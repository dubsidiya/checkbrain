def matchMask( s ):
  if not (s.startswith('123') and s.endswith('67') ):
    return False
  s = s[3:-2]
  if '45' not in s: return False
  pos = s.index('45')
  return all( c in '02468' for c in s[:pos] ) and \
         len(s[pos+2:]) == 1

from math import ceil
D = 257
start = ceil( 1234567/D ) * D
for n in range(start, 12390000000, D):
  if n % D == 0 and matchMask( str(n) ):
     print( n, n // D )
