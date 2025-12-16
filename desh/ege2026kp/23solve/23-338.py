from functools import cache
@cache
def f( start, end ):
  return 1 if start == end else \
         0 if start > end or start == 56 else \
         f(start+3,end) + f(start+7,end) + f(start*3,end)

print( f(12,40)*f(40,72)*f(72,89) )