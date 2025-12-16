
from time import time
startTime = time()

def isPrime(n):
  return all( n % d != 0
              for d in range(2,int(n**0.5)+1) )

palindroms = []
for i in range(1,99999+1):
  s0 = str(i)
  s = s0 + s0[::-1]
  if int(s) < 1000000000:
    palindroms.append(int(s))
  s = s0 + s0[-2::-1]
  if int(s) < 1000000000:
    palindroms.append(int(s))

print( 'Palindroms:', len(palindroms) )

primePal = [x for x in palindroms if isPrime(x)]
print( 'Prime palindroms:', len(primePal) )

def prodDigits( n ):
   p = 1
   while n:
     if n % 10 > 0: p *= n % 10
     n //= 10
   return p

byProdDigits = {}
for x in primePal:
  p = prodDigits(x)
  if p in byProdDigits:
    byProdDigits[p].append(x)
  else:
    byProdDigits[p] = [x]

byProdPairs = [ (p,byProdDigits[p]) for p in byProdDigits ]

maxPopulated = max( byProdPairs, key = lambda x: len(x[1]) )[1]
print( maxPopulated[-5:] )

print( "Время:", int(time() - startTime), "с" )