def matchMask( s ):
  return s[:2] == '14' and s[3] == '4'

def allDivs( n ):
    divs = set()
    for d in range(1,round(n**0.5)+1):
       if n % d == 0:
          divs.add( d )
          divs.add( n // d )
    return sorted(list(divs))

def valid( n ):
  return matchMask( str(n) ) and n % 217 == 0

n, count = 10**7-1, 0
results = []
while count < 7:
  if valid( n ):
    count += 1
    results.append( (n, sum( d for d in allDivs(n) if d % 2 == 1 )) )
  n -= 1

for n, s in results[::-1]:
  print( n, s )
