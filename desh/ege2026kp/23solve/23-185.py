
negResults = set()
def f( start, count ):
  if count == 0:
    if start < 0:
      negResults.add( start )
    return
  f( start-2, count-1 )
  f( start*(-3), count-1 )

f(91, 11)

print( len(negResults) )