def f( start, end ):
  return 1 if start == end else \
         0 if start < end or start == 8 else \
         f( start-1, end ) + f( start-4, end ) + f( start//3, end )

print( f(19,14)*f(14,2) )