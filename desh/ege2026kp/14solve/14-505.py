from itertools import product

def intt( digits, p ):
  digits = digits[::-1]
  N = len(digits)
  return sum( d*p**i for d, i in zip(digits, range(N)) )

p = 10
while True:
  print( p )
  found = False
  for x, y, z, w in product( range(p), repeat=4 ):
    if y*w == 0: continue
    r = intt( [y,0,9,x],p) + intt( [y,y,7,w],p) - intt([w,z,y,z,y],p)
    if r == 0 and len(set((x, y, z, w))) == 4:
      print( p, x, y, z, w, intt([x, y, z, w], p) )
      found = True
  if found: break
  p += 1

print( p )