def allDivs( n ):
  q = round(n**0.5)
  divs = []
  for d in range(2,q+1):
    if n % d == 0:
      divs.extend( [d, n // d] )
  return sorted( divs )

count = 0
n = 1_324_727 + 1
while count < 5:
  divs = allDivs( n )
  if len(divs) == 2 and '5' in str(divs[0]) and \
     '5' in str(divs[1]):
    print( n, divs[1] )
    count += 1
  n += 1
