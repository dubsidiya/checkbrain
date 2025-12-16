def factor( n ):
   d = 2
   primes = []
   while d <= n:
     while n % d == 0:
       primes += [d]
       n //= d
     d += 1
   return primes

def valid( n ):
   divs = factor( n )
   D = 1
   for d in divs[1:]: D *= d
   S = sum(divs)
   Q = int( str(S)[::-1] )
   return D+Q if n+D+Q > 202122 else 0

n, count = 1000, 0
while count < 5:
  DpQ = valid( n )
  if DpQ > 0:
    count += 1
    print( n, DpQ )
  n += 1
