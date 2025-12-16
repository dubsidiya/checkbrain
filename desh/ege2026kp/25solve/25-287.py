from fnmatch import fnmatch

def allDivs( n ):
  a = set()
  for d in range(1, round(n**0.5) + 1):
    if n % d == 0:
      a.add( d )
      a.add( n // d )
  return sorted( a )

n = 0
while n < 10**7:
  s = str(n)
  if s == s[::-1] and fnmatch( s, '*2?2*' ):
    divs = allDivs( n )
    if len(divs) > 30:
      print( n, sum(divs) )
  n += 53


