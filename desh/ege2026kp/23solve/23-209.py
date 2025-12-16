def f( start, end, nCmd = 0 ):
  return 0 if start > end else \
         nCmd % 2 if start == end else \
         f( start+2, end, nCmd+1 ) + f( start*2, end, nCmd+1 ) + \
            (f( start*start, end, nCmd+1 ) if start > 1 else 0)

print( f(1, 100) )