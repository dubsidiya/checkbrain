def f( start, end ):
  if start < end: return 0
  if start == end: return 1
  return f(start-2, end) + f(start//2, end)

print( f(38,16)*f(16,2) )

#------------------------------------

def f( start, end, hit16 = 0 ):
  if start < end: return 0
  if start == end: return hit16
  if start == 16: hit16 = 1
  return f(start-2, end, hit16) + f(start//2, end, hit16)

print( f(38,2) )
