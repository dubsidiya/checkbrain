
def oddDivs( n ):
  divs = set()
  if n % 2 == 0: return []
  for d in range(3, round(n**0.5)+1, 2):
    if n % d == 0:
       divs |= { d, n//d }
  return sorted(divs)

for n in range(321655, 654321+1, 2):
  divs = oddDivs(n)
  if len(divs) > 70:
    print( n, divs[-1] )
