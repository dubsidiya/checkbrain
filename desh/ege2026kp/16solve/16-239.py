from sys import setrecursionlimit

setrecursionlimit(2000)
def F( n ):
  return 3 if n < 3 else \
         2*n + 6 + F(n-2)

print( F(3027) - F(3023) )