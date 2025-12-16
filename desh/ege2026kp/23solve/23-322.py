def f( start, end ):
  if start > end or start == 13: return 0
  if start == end: return 1
  return f(start+2, end) + f(start*3, end) + f(start**2, end)

print( f( 3, 49 ) )
