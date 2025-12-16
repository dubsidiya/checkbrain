def f( start, end, nOdd = -1 ):
  if start > end or nOdd > 6: return 0
  if start == end: return 1
  nOdd = 0 if nOdd < 0  else \
         nOdd + (start % 2 != 0)
  return f( start+2, end, nOdd ) + \
         f( start*2, end, nOdd ) + \
         f( start*3, end, nOdd )

N = 214
print( f( 1, N ) )

