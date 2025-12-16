from fnmatch import fnmatch

results = []

for n in range( 0, 10**10, 18579 ):
  if fnmatch( str(n), '54?1?3*7' ):
    print( n, n//18579 )
