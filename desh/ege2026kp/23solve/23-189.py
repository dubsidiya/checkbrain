def f( way, end ):
  last = way[-1]
  return 0 if abs(last) > 40 or way.count(last) > 1 else \
         1 if last == end \
         else f( way+[last+2], end ) + f( way+[last-3], end )

print( f( [1], 30 ) )

