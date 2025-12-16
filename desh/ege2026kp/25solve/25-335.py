def valid( n ):
  q = round(n**0.5)
  divs9 = []
  for d in range(2,q+1):
    if n % d == 0:
      if d > 10 and d % 10 == 9:
        divs9.append( d )
      if (n//d) > 10 and (n//d) % 10 == 9:
        divs9.append( n//d )
  return (True, min(divs9)) if divs9 else (False, 0)

results = []
for n in range(800_001, 900_000):
  ok = valid(n)
  if ok[0]:
    results.append( (n, ok[1]) )
    if len(results) >= 5: break

for r in results:
  print( r[0], r[1] )

print('----------------------------------')

def allDivs(n):
  divs = set()
  for i in range(2, int(n**0.5)+1):
   if n%i == 0:
     divs |= { i, n//i }
  return sorted(divs)

count = 0
for i in range(800_001, 900_000):
  divs9 = [ d for d in allDivs(i)
              if d != 9 and d % 10 == 9 ]
  if divs9:
    print( i, min(divs9) )
    count += 1
    if count >= 5:
      break
