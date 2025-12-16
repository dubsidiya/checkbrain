def f( start, end ):
  return 1 if start == end else \
         0 if start > end or start == 20 else \
         f( start+1, end ) + f( start+2, end ) + f( start**2, end )

print( f(6, 18) * f(18, 27) )

def f1( start, end ):
  return 1 if start == end else \
         0 if start < end or start == 20 else \
         f1( start-1, end ) + f1( start-2, end ) + \
         (f1( round(start**0.5), end ) if start**0.5 % 1 == 0 else 0)

print( f1(27, 18)*f1(18, 6) )