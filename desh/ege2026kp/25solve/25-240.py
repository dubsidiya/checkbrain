def matchMask( s ):
  return s[0] == '9' and s[-1] == '7' and '55' in s \
         and s.index('55') > 1

def allDivs( n ):
    divs = set()
    for d in range(1,round(n**0.5)+1):
       if n % d == 0:
          divs.add( d )
          divs.add( n // d )
    return sorted(list(divs))

def valid( n ):
  return matchMask( str(n) )

n, count = 10**7, 0
results = []
while count < 5:
  if valid(n):
    count += 1
    results.append( (n, sum(allDivs(n)) % 21) )
  n -= 1

for n, s in results[::-1]:
  print( n, s )
