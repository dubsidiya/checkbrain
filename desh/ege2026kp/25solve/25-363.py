def isPrime( n ):
  q = round(n**0.5)
  return n == 2 or \
         (n > 1 and all( n % d != 0 for d in range(2,q+1) ) )

def allPrimeDivs( n ):
  q = round(n**0.5)
  divs = set()
  for d in range(2,q+1):
    if n % d == 0:
      if isPrime(d): divs.add( d )
      if isPrime(n//d): divs.add( n//d )
  return sorted( divs )

def getM( n ):
  pDivs = allPrimeDivs( n )
  return pDivs[0]+ pDivs[-1] if pDivs else 0

def isPalindrome( n ):
  s = str(n)
  return s == s[::-1]

count = 0
n = 5_400_000 + 1
while count < 5:
  M = getM( n )
  if M > 60_000 and isPalindrome(M):
    print( n, M )
    count += 1
  n += 1
