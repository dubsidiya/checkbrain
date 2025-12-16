from functools import cache
@cache
def f( start, end ):
  return 1 if start == end else \
         0 if start > end or start == 8 else \
         f(start+1,end) + f(start+2,end) + f(start*2,end)

print( f(3,14)*f(14,18) )