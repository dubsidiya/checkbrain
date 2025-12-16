from functools import lru_cache

@lru_cache
def f( start, end, n14 = 0 ):
  n14 += sum( map(int, str(start)) ) == 14
  if start == end:
    return 1 if n14 == 5 else 0
  elif start > end or n14 > 5:
    return 0
  else:
    return f(start+2, end, n14) + \
           f(start*3, end, n14) + \
           f(start*4, end, n14)

print( f( 1, 600 ) )