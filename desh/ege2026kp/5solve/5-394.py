from string import digits, ascii_uppercase

alpha = digits + ascii_uppercase

def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + alpha[n%b]

def alg( n ):
  s = tobase(n, 20)
  sNew = ''
  for c in s:
    sNew += alpha[(int(c,20)+1)%20]
  sNew = str(n%2) + sNew
  return tobase(int(sNew,20), 20)

def valid( s ):
  return len(s) >= 3 and \
         sum( c > '9' for c in s ) >= 2

for n in range(1000):
  r = alg(n)
  if valid(r):
    print( n )
    break
