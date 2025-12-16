def f( start, end, bitCode = 0 ):
  return 0 if start > end or (start == end and bitCode != 7) else \
         1 if start == end else \
         f( start+1, end, bitCode | 1 ) + \
           f( start+2, end, bitCode | 2 ) + \
           f( start*2, end, bitCode | 4 )

print( f( 3, 25 ) )
