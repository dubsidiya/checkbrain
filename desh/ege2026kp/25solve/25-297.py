from fnmatch import fnmatch

def allDivs( n ):
  q = round( n**0.5 )
  divs = set()
  for d in range(1,q+1):
    if n % d == 0:
       divs |= { d, n//d }
  return sorted(divs)

D = 3131

for n in range(D, 10**6, D):
  divs = [d for d in allDivs(n)
                 if fnmatch(str(d), "2*5*") ]
  if len(divs) == 3:
     print( n, divs[-1] )
