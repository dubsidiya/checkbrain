results = set()
def f( start, cmd ):
  if cmd == 0:
    results.add( start )
    return
  f( start-1, cmd-1 )
  f( start-2, cmd-1 )
  if start >= 0 and start**0.5 % 1 == 0:
    f( round(start**0.5), cmd-1 )

f(113, 17)

print( len(results) )
