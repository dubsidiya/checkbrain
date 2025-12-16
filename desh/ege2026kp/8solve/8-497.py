from itertools import *

def valid( s ):
  for c in '02468':
    s = s.replace( c, '*' )
  nPairs = sum( s[i] == '*' and s[i+1] == '*'  for i in range(len(s)-1) )
  return nPairs == 2 and '***' not in s

no = 0
count = 0
for w in product('01234', repeat=9):
  if w[0] != '0':
    no += 1
    w = ''.join( w )
    if valid( w ):
      count += 1

print( count )