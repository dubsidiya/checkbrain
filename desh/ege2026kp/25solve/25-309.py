def sumDigits( n ):
  return sum( map(int, str(n)) )

def valid( n ):
  s = str(n)
  sd = sumDigits(n)
  return s.startswith('20') and s.endswith('23') and sd in [7,14]

for n in range(0, 10**9, 2023):
  if valid(n):
    print( n, n // 2023 )