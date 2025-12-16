def f( start, end ):
  return 0 if start < end else \
         1 if start == end else \
         f( start-3, end ) + f( start//7, end )

print( f( 50, 1 ) )
