def digRoot( n ):
  if n < 10: return n
  return digRoot( sum(map(int, str(n))) )

def f( start, end, prog ):
  prog = prog + [start]
  if len(prog) > 1 and digRoot(prog[-2]) == start % 10:
    return 0
  if start > end: return 0
  if start == end: return 1
  return f( start+1, end, prog ) + f( start+2, end, prog )

print( f( 12, 37, [] ) )