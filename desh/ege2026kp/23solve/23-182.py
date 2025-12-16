
def f( start, end, count = 0 ):
  return 1 if start == end else \
         0 if start > end else \
         f( start+2, end, count ) + \
          ( f( start*2, end, count ) if start % 2 == 1 else 0 ) + \
          ( f( start*2+1, end, count+1 ) if count < 2 and start % 2 == 0 else 0 )

print( f(2, 35) )