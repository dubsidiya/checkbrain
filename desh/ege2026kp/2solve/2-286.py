def F( x, y, z, w ):
  return int( (x == (y <= z)) and (y == (not (z <= w))) )

from itertools import product, permutations

for x, y, z, w in product([0,1], repeat=4):
  if F(x, y, z, w):
    print( x, y, z, w, F(x, y, z, w) )

from itertools import product, permutations

values = [1, 1, 1]
for a, b, c, d, e in product([0,1], repeat=5):
  table = [ (1, e, 0, b),
            (0, 1, d, c),
            (1, 0, 0, a), ]
  if len(table) != len(set(table)): continue
  for p in permutations("xyzw"):
    valP = [ F(**dict(zip(p, row))) for row in table ]
    if valP == values:
      print( ''.join(p) )
