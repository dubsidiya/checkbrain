from itertools import product

def intt( digits, p ):
  digits = digits[::-1]
  N = len(digits)
  return sum( d*p**i for d, i in zip(digits, range(N)) )

for p in range(10,250):
  print( p )
  found = False
  for x, y, z, w in product( range(p), repeat=4 ):
    if y*w == 0: continue
    r = intt( [y,0,7,x],p) + intt( [w,y,9,z],p) - intt([z,x,y,x,y],p)
    if r == 0 and len(set((x, y, z, w))) == 4:
      print( p, x, y, z, w, intt([x, y, z, w], p) )
      found = True
      break
  if found: break

print( p )