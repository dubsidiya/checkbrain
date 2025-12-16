def f( start, end ):
  if start == end: return 1
  if start > end or start == 58: return 0
  return f( start+1, end ) + f( start+2, end ) + \
         f( start+3, end ) + f( start*4, end )

print( f(38, 45)*f(45, 68))