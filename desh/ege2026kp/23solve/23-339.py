from functools import cache
@cache
def f( start, end ):
  return 1 if start == end else \
         0 if start > end or start == 9 else \
         f(start+1,end) + f(start*2,end) + f(start*3,end)

print( f(1,14)*f(14,16) )