from functools import cache

@cache
def f( start, end ):
  if start > end or start in [20, 25]: return 0
  if start == end: return 1
  return f( start+1, end ) + \
         f( start*2, end ) + \
         f( start*start, end )

count = f(2, 15)*f(15, 35)*f(35, 50)
print( count )
