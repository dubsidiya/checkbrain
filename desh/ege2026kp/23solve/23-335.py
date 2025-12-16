def f( start, end, prog = [] ):
  if start < end: return 0
  if start == end:
     return 19 in prog and 29 in prog and 24 not in prog
  prog = prog + [start]
  return f(start-1, end, prog) + f(start-6, end, prog) + \
         f(start//2, end, prog)

print( f(34, 6) )