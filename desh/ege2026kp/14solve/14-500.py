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

N = 153
for x in range(N):
  n = Number('BA3x98ADF', N, x) * Number('C1x78A75', N, x)
  if n % (N-1) == 0:
    print( x, Number('5xA', N, x) )