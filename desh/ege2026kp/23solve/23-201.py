def f( start, end, nEven = -1 ):
  if start > end or nEven > 2: return 0
  if start == end: return 1
  nEven = 0 if nEven < 0  else \
          nEven + (start % 2 == 0)
  return f( start+2, end, nEven ) + \
         f( start*2, end, nEven ) + \
         f( start*3, end, nEven )

N = 402
print( f( 1, N ) )

