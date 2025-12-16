import sys

sys.setrecursionlimit( 2500 )

def F( n ):
  return F(n//2) + 5 if n % 2 == 0 else \
         F(n//5) + 2 if n % 5 == 0 else \
         0

res = set()
for n in range(1,1000000+1):
  r = F(n)
  res.add( r )

print( len(res) )

