
def f( start, end ):
  if start < end or start == 22: return 0
  if start == end: return 1
  return f( start-2, end ) + f( start//2, end ) + f( start//3, end )

print( f(40, 2) )