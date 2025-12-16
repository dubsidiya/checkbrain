def allDivs(n):
  divs = set()
  for i in range(2, int(n**0.5)+1):
   if n%i == 0:
     divs |= { i, n//i }
  return sorted(divs)

results = []
for i in range(800_000, 900_000):
  divs = allDivs(i)
  M = divs[0] + divs[-1] if len(divs) >= 2  else 0
  if M % 10 == 4:
    results.append( (i, M) )
    if len(results) >= 5:
      break

for r in sorted(results):
  print( r[0], r[1] )
