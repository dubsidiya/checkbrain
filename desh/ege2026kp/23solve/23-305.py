from functools import cache

@cache
def f( start, end ):
  if start > end or start == 20: return 0
  if start == end: return 1
  return f( start+1, end ) + \
         f( start+3, end ) + \
         f( start*start, end )

count = f(2, 15)*f(15, 35)
print( count )
