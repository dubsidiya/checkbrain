from fnmatch import fnmatch

D = 8993
mask = '89*4?5?7?'

for n in range(0, 10**10, D):
  if fnmatch( str(n), mask ):
    print( n, n // D )
