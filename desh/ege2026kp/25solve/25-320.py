
def allDivs( n ):
  divs = set()
  for d in range(1, int(n ** 0.5) + 1):
    if n % d == 0:
      divs.add( d )
      divs.add( n // d )
  return sorted(divs)

def valid( n ):
  d = [ x for x in allDivs( n ) if x % 2 == 0 ]
  s = str(n)
  return len(d) >= 4 and s[0] == '6' and s[-2] == '5' and '97' in s, \
         sum(d)

count = 0
for n in range(65050, 70000):
  isValid, s = valid( n )
  if isValid:
    print( n, s )
    count += 1

for n in range(600050, 700000):
  isValid, s = valid( n )
  if isValid:
    print( n, s )
    count += 1
    if count >= 7: break
