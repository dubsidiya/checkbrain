from fnmatch import fnmatch

D = 1917
mask = '3?12?14*5'

for n in range(0, 10**10, D):
  if fnmatch( str(n), mask ):
    print( n, n // D )
