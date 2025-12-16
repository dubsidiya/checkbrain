def f( start, end ):
  return 0 if start < end else \
         1 if start == end else \
         f( start-1, end ) + f( start // 2, end )

print( f(30, 12) * f(12, 1) )