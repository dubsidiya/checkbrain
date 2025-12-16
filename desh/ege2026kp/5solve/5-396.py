from string import digits, ascii_uppercase

alpha = digits + ascii_uppercase

def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + alpha[n%b]

def alg( n ):
  s = tobase(n, 19)
  sumDigits = sum( alpha.index(c) for c in s )
  if sumDigits % 2 == 0:
    s = s[-1] + s[:-1] + '1'
  else:
    s = 'B' + s[1:] + s[0]
  return int(s,19)

count = 0
for n in range(1,10000+1):
  r = alg(n)
  if (r % 5 == 0) != (r % 3 == 0):
    count += 1
print( count )
