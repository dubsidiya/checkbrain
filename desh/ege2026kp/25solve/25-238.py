def isPrime( n ):
   return all( n % d != 0 for d in range(2,round(n**0.5)+1) )

def valid( n ):
   if not isPrime(n): return False, 0
   s = str(n)
   L = len(s)
   primes = set()
   for i in range(L):
     for j in range(i+1,L):
       if s[i] != s[j]:
          s1 = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
          if isPrime( int(s1) ):
            primes.add( int(s1) )
   if len(primes) >= 12:
      #print( n, end = " ")
      #for n1 in primes:
      #  print( n1, end = " ")
      #print()
      return True, max(primes)
   return False, 0

n, count = 1411111111, 0
while count < 5:
  isValid, maxPrime = valid(n)
  if isValid:
    print( n, maxPrime )
    count += 1
  n += 1