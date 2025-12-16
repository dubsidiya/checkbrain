def isPrime( n ):
  return n == 2 or \
         all( n % d != 0 for d in range(2, round(n**0.5)+1) )

for i in range (0, 10**8, 311):
  s = str(i)
  if s[:2] == "12" and s[3] == '5' and s[-3] == '5' and isPrime(i//311):
        print( i, i // 311)