from string import ascii_uppercase, digits
A = digits + ascii_uppercase
def toBase( n, b ):
   s = ''
   while n:
     s = A[n % b] + s
     n //= b
   return s
for X in range(int('1C0',32), int('1D0',32)):
  X32 = toBase( X, 32 )
  X16 = toBase( X, 16 )
  X8 =  toBase( X, 8 )
  if len(X16) == 3 and len(X8) == 4 and X16[-1] == 'D' and \
     X8[-2] == '3':
    print( X )