def f( start, end ):
  return 1 if start == end else \
         0 if start > end else \
         f( start+2, end ) + f( start+4, end ) + f( start**2, end )

print( f(2, 12) * f(12, 32) * f(32, 46) )