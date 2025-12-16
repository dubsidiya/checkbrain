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

N = 97
for x in range(N):
  n = Number('A7FxDA6F3', N, x) * Number('A1xDE052', N, x)
  if n % (N-1) == 0:
    print( x, Number('4xB', N, x) )