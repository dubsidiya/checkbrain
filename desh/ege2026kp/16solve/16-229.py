import sys

sys.setrecursionlimit( 2500 )

def F( n ):
  return F(n//2) + 5 if n % 2 == 0 else \
         F(n//5) + 2 if n % 5 == 0 else \
         0

n = 1
res = set()
while True:
  r = F(n)
  if not r in res:
    #print( n, r )
    res.add( r )
  if r == 130: break
  n += 1
print( n, r )

