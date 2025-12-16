def f( start, end ):
  if start < end: return 0
  if start == end: return 1
  return f(start-2, end) + f(start//2, end)

print( f(32,14)*f(14,1) )

#------------------------------------

def f( start, end, hit14 = 0 ):
  if start < end: return 0
  if start == end: return hit14
  if start == 14: hit14 = 1
  return f(start-2, end, hit14) + f(start//2, end, hit14)

print( f(32,1) )
