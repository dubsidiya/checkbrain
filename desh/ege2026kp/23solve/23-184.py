
posResults = set()
def f( start, count ):
  if count == 0:
    if start > 0:
      posResults.add( start )
    return
  f( start-3, count-1 )
  f( start*(-3), count-1 )

f(133, 9)

print( len(posResults) )