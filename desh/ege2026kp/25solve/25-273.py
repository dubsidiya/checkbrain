def allDivs(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d |= {i, x//i}
    return sorted(d)

def coprime( a, b ):
  for i in range(2, min(a, b)+1):
    if a % i + b % i == 0: return False
  return True

def check( n ):
  divs = allDivs(n)
  if len(divs) >= 6:
    div6 = divs[:6]
    OK = all( coprime(a,b) for a in div6 for b in div6 if a != b )
    if OK:
       return (n, divs[-1])

n = 1_000_000_000
res = []
while len(res) < 5:
  r = check(n)
  if r:
    res.append( r )
    print( f'found: {len(res)}')
  n -= 1

for r in sorted(res):
  print( r[0], r[1] )