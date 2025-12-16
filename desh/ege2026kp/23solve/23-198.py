def f( start, end, diff = 0 ):
  if start == end:
    return 1 if diff > 0 else 0
  if start > end: return 0
  count = f( start+1, end, diff-1 ) + \
          f( start*2, end, diff+1 ) + f( start*3, end, diff+1 )
  return count

print( f(1, 157) )

