def sumDivs( n ):
  divs = set()
  for d in range(1,round(n**0.5)+1):
    if n % d == 0:
      divs.add( d )
      divs.add( n//d )
  return sum(divs)

count = 0
n = 500000 + 1
while count < 5:
  sd = sumDivs(n)
  if str(sd)[-2] == '7':
    print( n, sd )
    count += 1
  n += 1