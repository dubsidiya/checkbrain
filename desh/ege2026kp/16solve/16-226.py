import sys

sys.setrecursionlimit( 2500 )

def f( n ):
  return 1 if n < 3 else (n-1)*f(n-2)


print( (f(2026) - 5*f(2024)) / f(2022) )

