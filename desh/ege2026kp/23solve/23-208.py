def f( start, end ):
  return 0 if start < end else \
         1 if start == end else \
         f( start-2, end ) + f( start // 2, end )

print( f(28, 10) * f(10, 1) )