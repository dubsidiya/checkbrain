def f( start, end ):
  if start == end: return 1
  if start > end: return 0
  return f( start+1, end ) + f( 10*start+1, end )

print( f(1, 555) )

