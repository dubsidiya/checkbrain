def f( start, end, nDiv6 = -1 ):
  if start > end or nDiv6 > 3: return 0
  if start == end: return 1
  nDiv6 = 0 if nDiv6 < 0  else \
         nDiv6 + (start % 6 == 0)
  return f( start+2, end, nDiv6 ) + \
         f( start*2, end, nDiv6 ) + \
         f( start*3, end, nDiv6 )

N = 300
print( f( 1, N ) )

