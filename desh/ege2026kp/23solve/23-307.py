from functools import cache

@cache
def f( start, end ):
  if start > end or start in [15, 35]: return 0
  if start == end: return 1
  return f( start+1, end ) + \
         f( start*2, end ) + \
         f( start*start, end )

count = f(2, 20)*f(20, 60)*f(60, 100)
print( count )
