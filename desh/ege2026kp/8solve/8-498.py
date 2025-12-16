from itertools import *

def valid( s ):
  if not s: return False
  n = int(s,3)
  sumDigits = sum( map(int, s) )
  for c in '02':
    s = s.replace( c, '*' )
  nPairs = sum( ( s[i] == '*' and s[i+1] == '1' or \
                  s[i] == '1' and s[i+1] == '*' )
                  for i in range(len(s)-1) )
  return nPairs > 3 and n % sumDigits == 0

count = 0
for w in product('012', repeat=12):
  w = ''.join( w ).lstrip('0')
  if valid( w ):
    count += 1

print( count )