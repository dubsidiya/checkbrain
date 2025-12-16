from itertools import *

def valid( s ):
  for c in '13579B':
    s = s.replace( c, '*' )
  return '**' not in s

count = 0
no = -1
for w in product('0123456789ABC', repeat=3):
  if w[0] != '0':
    no += 1
    w = ''.join( w )
    if valid( w ) and no % 10 == 7:
      count += 1

print( count )
