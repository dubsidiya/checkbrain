from functools import lru_cache

@lru_cache
def f( start, end, lastCmd ):
  if start == end: return 1
  if start == 28 or start > end: return 0
  count =  f( start+1, end, 1 ) if lastCmd != 1 else 0
  count += f( start+3, end, 2 ) if start not in [8,9] else 0
  count += f( start*2, end, 3 ) if not(6<=start<=9) else 0
  return count

print( f( 4, 93, 0 ) )