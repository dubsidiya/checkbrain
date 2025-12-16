def allDivs(n):
  divs = set()
  for i in range(2, int(n**0.5)+1):
   if n%i == 0:
     divs |= { i, n//i }
  return sorted(divs)

count = 0
for i in range(700_001, 800_000):
  divs = allDivs(i)
  M = divs[0] + divs[-1] if len(divs) >= 2  else 0
  if M % 100 == 14:
    print( i, M )
    count += 1
    if count >= 5:
      break
