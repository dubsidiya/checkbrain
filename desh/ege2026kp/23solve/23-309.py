from functools import cache

@cache
def f( start, end ):
  if start > end or start in [17, 32, 50]: return 0
  if start == end: return 1
  return f( start+1, end ) + \
         f( start+5, end ) + \
         f( start*start, end )

count = f(5, 25)*f(25, 45)*f(45, 60)
print( count )
