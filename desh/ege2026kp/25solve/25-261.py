def match( n ):
  s = str(n)
  ind1 = [ i for i, c in enumerate(s) if c == '1' ]
  ind68 = [ i for i, c in enumerate(zip(s,s[1:])) if c == ('6','8') ]
  for i in ind1:
    for j in ind68:
      if j-i >= 3: return True
  return False

n = 10068
while not( match(n) and n % 161 == 0 ):
  n += 1

count = 0
while n <= 17*10**6:
  if match(n) and n % 161 == 0:
    count += 1
    if count % 500 == 1:
      print( n, n // 161 )
  n += 161



