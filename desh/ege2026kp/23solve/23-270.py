def f( start, end ):
  if start > end or start == 23:
    return 0
  if start == end:
    return 1
  return f( start+2, end ) + f( start*3, end ) + f( start*5, end )

print( f(1, 13)*f(13, 75) )