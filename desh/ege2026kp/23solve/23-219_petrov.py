# Автор: В. Петров

k = 30
end = 9217

from functools import lru_cache
@lru_cache(None)
def f( start, end, count1 ):
  if start > end or count1 > k: return 10**10
  if start == end and count1 == k: return 0
  return min( f(start+1, end, count1+1),
              f(start*2, end, count1),
              f(start*3, end, count1) ) + 1

print( f(1, end, 0) )
