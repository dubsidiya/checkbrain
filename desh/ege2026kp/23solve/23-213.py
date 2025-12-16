from functools import lru_cache

@lru_cache
def f( start, end, prev = None ):
  if prev != None and \
     (prev % 2 == 1 and start % 2 == 1):
     return 0
  if start == end:  return 1
  elif start > end: return 0
  else:
    return f(start+2, end, start) + \
           f(start*3, end, start) + \
           f(start*4, end, start)

print( f( 1, 600 ) )