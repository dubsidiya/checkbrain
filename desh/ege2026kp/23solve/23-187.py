
def f( start, end, count = 0 ):
  return 1 if start == end else \
         0 if start > end else \
         f(start+2, end, count) + f(start+3, end, count) + \
          ( f(start*2, end, count+1) \
            if start % 2 == 1 and count < 2 else 0 )

print( f( 3, 46 ) )