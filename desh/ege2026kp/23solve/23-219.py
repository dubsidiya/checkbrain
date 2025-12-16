from functools import cache

k1 = 30
end = 9217

minLen = 100000

@cache
def f( start, end, count1 = 0, L = 0 ):
   global minLen
   if start > end or L >= minLen or count1 > k1: return
   if start == end:
      if count1 == k1: minLen = min( minLen, L )
      return
   f( start+1, end, count1+1, L+1 )
   f( start*2, end, count1, L+1 )
   f( start*3, end, count1, L+1 )

f( 1, end )
print( minLen )