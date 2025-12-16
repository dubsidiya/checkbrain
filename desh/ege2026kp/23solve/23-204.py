def f( n1, n2, S ):
  if n1 + n2 > S: return 0
  if n1 + n2 == S: return 1
  return f( n1+n2, n2, S ) + f( n1, n1+n2, S )

print( f( 1, 1, 88 ) )

