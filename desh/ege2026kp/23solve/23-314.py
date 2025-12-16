from functools import cache

@cache
def f( start, end, lastCmd = 0, hit60 = False ):
  if start > end+5 or start % 10 == 3: return 0
  if start == end: return hit60
  if start == 60: hit60 = True
  total = 0 if lastCmd == 1 else \
          f( start-1, end, 1, hit60 ) + f( start-5, end, 1, hit60 )
  return total + \
         f( start+7, end, 3, hit60 ) + f( start*2, end, 4, hit60 )

count = f(9, 84)
print( count )
