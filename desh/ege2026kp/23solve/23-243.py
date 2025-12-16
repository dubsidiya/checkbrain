
def f( start, end, prog = None ):
  if prog is None: prog = []
  if start not in range(40, 50) or \
     prog.count(start) > 1:
    return 0
  if prog and start == end: return 1
  return f( start+1, end, prog+[start+1] ) + \
         f( start+3, end, prog+[start+3] ) + \
         f( start-1, end, prog+[start-1] ) + \
         f( start-3, end, prog+[start-3] )

print( f(42, 42) )