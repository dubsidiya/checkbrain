from functools import cache

@cache
def f( start, end, lastCmd = 0, hit26 = False ):
  if start > end+10 or start % 10 == 1: return 0
  if start == end: return hit26
  if start == 26: hit26 = True
  total = 0 if lastCmd == 1 else \
          f( start-1, end, 1, hit26 ) + f( start-3, end, 1, hit26 )
  return total + \
         f( start+6, end, 3, hit26 ) + f( start*3, end, 4, hit26 )

count = f(5, 58)
print( count )
