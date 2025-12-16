from string import digits, ascii_uppercase

A = digits + ascii_uppercase

def toBase( n, base ):
  s = ''
  while n:
    s = A[n%b] + s
    n //= b
  return s

for n in range(2023, 2023**2+1):
  s = str(n)
  if s[:2] == '20' and s[-2:] == '23':
    bPal = []
    for b in range(2,37):
      s = toBase( n, b )
      if s == s[::-1]:
        bPal += [b]
    if len(bPal) > 1:
      print( n, sum(bPal), bPal )