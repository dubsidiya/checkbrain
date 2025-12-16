from string import digits, ascii_uppercase

def toNumber( digs, base ):
  n = 0
  for i, d in enumerate(digs[::-1]):
    n += d*base**i
  return n

A = digits + ascii_uppercase
def Number( s, base, x = 0 ):
  digs = []
  for c in s:
    digs.append( x if c == 'x' else A.index(c) )
  return toNumber( digs, base )

for x in range(37):
  n = Number('F53xA1DEB', 37, x) * Number('C3xDE052', 37, x)
  if n % 36 == 0:
    print( x, Number('2x5', 37, x) )