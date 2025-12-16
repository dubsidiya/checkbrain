from functools import lru_cache

@lru_cache
def f( start, end, lastCmd ):
  if start == end: return 1
  if start in [12,20] or start > end: return 0
  count =  f( start+1, end, 1 )
  count += f( start+2, end, 2 ) if start not in [14,29] else 0
  count += f( start*3, end, 3 ) if lastCmd != 3 and \
                                   not(6<=start<=14) and \
                                   not(11<=start<=29) else 0
  return count

print( f( 2, 38, 0 ) )