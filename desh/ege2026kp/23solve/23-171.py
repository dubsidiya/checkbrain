from functools import lru_cache

@lru_cache
def f( start, end, lastCmd ):
  if start == end: return 1
  if start == 23 or start > end: return 0
  count =  f( start+1, end, 1 ) if lastCmd != 1 else 0
  count += f( start+2, end, 2 ) if start != 10 else 0
  count += f( start*2, end, 3 ) if not(6<=start<=10) else 0
  return count

print( f( 3, 79, 0 ) )