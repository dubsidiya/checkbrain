from functools import cache

@cache
def f( start, end, lastCmd = 0, hit30 = False ):
  if start > end+1 or start == 20: return 0
  if start == end: return hit30
  if start == 30: hit30 = True
  total = 0 if lastCmd == 1 else \
          f( start-1, end, 1, hit30 )
  return total + \
         f( start+2, end, 2, hit30 ) + \
         f( start*2, end, 3, hit30 )

print( f(3, 40) )
