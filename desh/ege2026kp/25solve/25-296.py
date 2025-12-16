from fnmatch import fnmatch

D = 50068
for n in range(D, 10**10, D):
  s = str(n)
  if '0' in s and fnmatch( s, "9?979*8" ):
     print( n, n//50068 )
