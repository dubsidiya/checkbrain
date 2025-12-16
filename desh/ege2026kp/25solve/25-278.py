def allDivs( n ):
  divs = set()
  for d in range(1, round(n**0.5)+1):
    if n % d == 0:
      divs.add( d )
      divs.add( n // d )
  return sorted( divs )

ends = [ '11', '22', '33', '44', '55', '66', '77', '88', '99' ]
for k in range(0, 4+1):
  for m in range(0, 10**(k+1)):
    for e in ends:
      fmt = "{{:0{}}}".format(k+1)
      n = int(e + fmt.format( m ) + e)
      q = round(n**0.5)
      if q*q == n:
        divs = allDivs( n )
        if len(divs) == 117:
          print( n, divs[-2] )









