
def allDivs( n ):
  divs = set()
  for d in range(2, round(n**0.5)+1):
    if n % d == 0:
      divs.add( d )
      divs.add( n // d )
  return sorted( divs )

def coprime( a, b ):
  for d in range(2, min(a, b)+1):
    if a % d == 0 and b % d == 0: return False
  return True

def valid( n ):
  divs = allDivs( n )
  last = divs[-1]
  divs = divs[:6]
  if len(divs) < 6: return False
  for i, d1 in enumerate(divs):
    for d2 in divs[i+1:]:
      if not coprime( d1, d2): return False
  return last

n = 2023
count = 0
while count < 5:
  res = valid( n )
  if res:
    print( n, res )
    count += 1
  n += 2023

mem = []
count = 0
n = 2023*( 10**9 // 2023 )
while count < 5:
  res = valid( n )
  if res:
    mem.append( (n, res) )
    count += 1
  n -= 2023

for m in sorted(mem):
  print( *m )






