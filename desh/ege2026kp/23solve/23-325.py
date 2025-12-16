def f( start, end ):
  if start > end: return 0
  if start == end: return 1
  return f(start+1, end) + f(start+2, end) + f(start+3, end)

print( f(5,7)*f(7,11) )

#------------------------------------

def f( start, end, hit7 = 0 ):
  if start > end: return 0
  if start == end: return hit7
  if start == 7: hit7 = 1
  return f(start+1, end, hit7) + f(start+2, end, hit7) + f(start+3, end, hit7)

print( f(5,11) )
