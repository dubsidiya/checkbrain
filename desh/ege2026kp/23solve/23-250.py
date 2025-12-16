def f( start, prog, A, C ):
  if not prog: return start
  c, prog = prog[0], prog[1:]
  if c == '1':
    return f( start+3, prog, A, C )
  if c == '2':
    return f( start*A, prog, A, C )
  if c == '3':
    return f( start+C, prog, A, C )

for A in range(2,101):
 for C in range(1,101):
    if f( 5, '1323123', A, C ) == 329:
      print( A, C, A+C )

