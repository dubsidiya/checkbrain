def f( start, end ):
  if start < end: return 0
  if start == end: return 1
  return f(start-2, end) + f(start//2, end)

print( f(32,8)*f(8,1) )

#------------------------------------

def f( start, end, hit8 = 0 ):
  if start < end: return 0
  if start == end: return hit8
  if start == 8: hit8 = 1
  return f(start-2, end, hit8) + f(start//2, end, hit8)

print( f(32,1) )
