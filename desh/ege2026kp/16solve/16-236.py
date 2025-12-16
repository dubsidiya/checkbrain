from sys import setrecursionlimit

setrecursionlimit(3000)

def F( n ):
  return 1 if n <= 5 else \
         n + F(n-2)

print( F(2126) - F(2122) )