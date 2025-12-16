from functools import cache

@cache
def f( start, end, lastCmd = 0, hit32 = False ):
  if start > end+1 or start in [10, 20, 30, 40, 50, 60]: return 0
  if start == end: return hit32
  if start == 32: hit32 = True
  total = 0 if lastCmd == 1 else \
          f( start-1, end, 1, hit32 )
  return total + \
         f( start+2, end, 2, hit32 ) + \
         f( start*3, end, 3, hit32 )

count = f(5, 62)
print( count )
