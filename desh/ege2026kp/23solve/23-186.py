
nonnegResults = set()
def f( start, count ):
  if count == 0:
    if start >= 0:
      nonnegResults.add( start )
    return
  f( start-5, count-1 )
  f( start*(-2), count-1 )

f(216, 7)

print( len(nonnegResults) )