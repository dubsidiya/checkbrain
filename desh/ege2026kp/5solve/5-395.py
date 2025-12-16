from string import digits, ascii_uppercase

alpha = digits + ascii_uppercase

def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + alpha[n%b]

def alg( n ):
  s = tobase(n, 20)
  L = len(s)
  if L % 2 == 0:
    s = s[-L//2:] + s[:L//2]
  else:
    s += s[-1]
  return int(s,20)

def valid( s ):
  return len(s) >= 3 and \
         sum( c > '9' for c in s ) >= 2

for n in range(1000):
  r = alg(n)
  if r > 190:
    print( n )
    break
