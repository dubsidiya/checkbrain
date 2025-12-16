import sys

sys.setrecursionlimit( 2500 )

def f( n ):
  return 1 if n < 3 else (n-1)*f(n-2)


print( (f(2025) - 2*f(2023)) / f(2021) )

