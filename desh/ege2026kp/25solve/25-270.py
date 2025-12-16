def allDivs(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d |= {i, x//i}
    return sorted(d)

def check( n ):
  divs = allDivs(n)
  if sum( 1 for d in divs if d % 2022 == 0 ) == 7:
    return ( n, max(divs) )

n = 100_000_000
res = []
while len(res) < 5:
  r = check(n)
  if r:
    res.append( r )
    print( f'found: {len(res)}')
  n += 1

n = 200_000_000
while len(res) < 10:
  r = check(n)
  if r:
    res.append( r )
    print( f'found: {len(res)}')
  n -= 1

for r in sorted(res):
  print( r[0], r[1] )