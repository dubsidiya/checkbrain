from fnmatch import fnmatch

for n in range(0, 10**8, 1923):
  if fnmatch( str(n), '1*2??76' ):
    print( n, n//1923 )


