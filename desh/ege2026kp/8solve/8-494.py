from itertools import *

def valid( s ):
  for c in '13579':
    s = s.replace( c, '*' )
  for c in '02468':
    s = s.replace( c, '.' )
  return '**' not in s and not '..' in s

no = 0
for w in product('0123456789', repeat=5):
  if w[0] != '0':
    no += 1
    w = ''.join( w )
    if valid( w ) and no % 15 == 0:
      print( no, w )
