from fnmatch import fnmatch

results = []

def A( n ):
  s = str(n)
  if (L := len(s)) % 2 == 1: return 0
  return (int(s[:L//2]) + int(s[L//2:]))**2

for n in range( 0, 35*10**6, 25 ):
  if fnmatch( str(n), "*2*0*2*5*" ) \
    and A(n) == n:
    print( n, n//25 )
