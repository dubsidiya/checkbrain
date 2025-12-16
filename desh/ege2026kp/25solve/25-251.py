def allDivs( n ):
  divs = set()
  for d in range(1, round(n**0.5)+1):
    if n % d == 0:
       divs.add( d )
       divs.add( n//d )
  return sorted(divs)

n = 800000 + 1
count = 0
while count < 6:
  divs = allDivs( n )
  oddDivs = [x for x in divs if x % 2 == 1]
  numOddDivs = len(oddDivs)
  if numOddDivs == len(divs) and numOddDivs > 10 and numOddDivs % 2 == 1:
    count += 1
    print( n, numOddDivs )
  n += 1
