from itertools import *

def valid( s ):
  for c in '1357':
    s = s.replace( c, '*' )
  return '**' not in s

no = 0
for w in product('012345678', repeat=6):
  if w[0] != '0':
    no += 1
    w = ''.join( w )
    if valid( w ) and no % 10 == 5:
      print( no, w )
