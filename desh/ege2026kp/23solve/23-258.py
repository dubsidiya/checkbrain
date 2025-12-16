def f( start, end, blocked = () ):
  if start > end or start in blocked:
    return 0
  if start == end: return 1
  return f( start+3, end, blocked ) + \
         f( start+5, end, blocked ) + \
         f( start*2, end, blocked )

print( f(4, 16) * f(16, 68, (32,)) +
       f(4, 32, (16,)) * f(32, 68) )
