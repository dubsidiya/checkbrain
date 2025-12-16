import sys

sys.setrecursionlimit( 2500 )

def F( n ):
  return F(n//2) + 5 if n % 2 == 0 else \
         F(n//3) + 4 if n % 3 == 0 else \
         0

n = 1
while F(n) != 108:
  n += 1
print( n )

