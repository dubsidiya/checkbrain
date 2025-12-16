def allDivs(n):
  divs = set( [1, n] )
  for i in range(2, int(n**0.5)+1):
   if n%i == 0:
     divs |= { i, n//i }
  return sorted(divs)

count = 0
for i in range(500_001, 600_000):
  divs = allDivs(i)
  R = sum( divs )
  if R % 10 == 6:
    print( i, R )
    count += 1
    if count >= 5:
      break
