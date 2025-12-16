def f( start, end ):
  return 1 if start == end else \
         0 if start > end else \
         f( start+2, end ) + f( start+3, end ) + f( start**2, end )

print( f(3, 25) )