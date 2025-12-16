from fnmatch import fnmatch

for n in range(0, 10**8, 2023):
  if fnmatch( str(n), '3?1*57' ):
    print( n, n//2023 )


