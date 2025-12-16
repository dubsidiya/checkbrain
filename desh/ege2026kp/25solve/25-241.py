def matchMask( s ):
  return s[1] == '6' and s[-1] == '6' \
         and '6' in s[2:-2]

def allDivs( n ):
    divs = set()
    for d in range(1,round(n**0.5)+1):
       if n % d == 0:
          divs.add( d )
          divs.add( n // d )
    return sorted(list(divs))

def valid( n ):
  return matchMask( str(n) ) and \
         n % 6 == 0 and n % 7 == 0 and n % 8 == 0

n, count = 16606, 0
while count < 7:
  if valid( n ):
    count += 1
    print( n, sum(allDivs(n))  )
  n += 1
