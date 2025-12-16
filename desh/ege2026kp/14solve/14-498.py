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

N = 57
for x in range(N):
  n = Number('F53xFE6D7', N, x) * Number('C3xDE052', N, x)
  if n % (N-1) == 0:
    print( x, Number('3xA', N, x) )