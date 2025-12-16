def f( start, end ):
  if start < end: return 0
  if start == end: return 1
  return f(start-1, end) + f(start-2, end) + f(start//3, end)

print( f(16,11)*f(11,6) )

#------------------------------------

def f( start, end, hit11 = 0 ):
  if start < end: return 0
  if start == end: return hit11
  if start == 11: hit11 = 1
  return f(start-1, end, hit11) + f(start-2, end, hit11) + \
         f(start//3, end, hit11)

print( f(16,6) )
