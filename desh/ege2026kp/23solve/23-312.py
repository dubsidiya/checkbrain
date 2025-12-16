from functools import cache

@cache
def f( start, end, lastCmd = 0, hit37 = False ):
  if start > end+2 or start in [5, 15, 25, 35, 45]: return 0
  if start == end: return hit37
  if start == 37: hit37 = True
  total = 0 if lastCmd == 1 else \
          f( start-1, end, 1, hit37 ) + f( start-2, end, 1, hit37 )
  return total + \
         f( start+5, end, 3, hit37 ) + f( start*2, end, 3, hit37 )

count = f(7, 50)
print( count )
