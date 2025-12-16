def matchMask( s ):
  return s[0] == '6' and s[-2] == '5' and '97' in s

def allDivs( n ):
    divs = set()
    for d in range(1,round(n**0.5)+1):
       if n % d == 0:
          divs.add( d )
          divs.add( n // d )
    return sorted(list(divs))

def valid( n ):
  if matchMask( str(n) ):
    evenDivs = [ x for x in allDivs(n) if x % 2 == 0 ]
    if len(evenDivs) >= 4:
      return True, sum(evenDivs)
  return False, 0

n, count = 65000, 0
while count < 7:
  OK, sumEvenDivs = valid( n )
  if OK:
    count += 1
    print( n, sumEvenDivs )
  n += 1