
def f( start, end ):
  return 1 if start == end else \
         0 if start > end else \
         f(start*2, end) if start % 2 == 1 else \
         f(start+1, end) + f(start+2, end)

print( f(2, 20)*f(20, 38)*f(38, 76) )