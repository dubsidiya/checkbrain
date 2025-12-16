from string import ascii_uppercase, digits
A = digits + ascii_uppercase
def toBase( n, b ):
   s = ''
   while n:
     s = A[n % b] + s
     n //= b
   return s
for X in range(2*8**3, 3*8**3):
  X32 = toBase( X, 32 )
  X16 = toBase( X, 16 )
  X8 =  toBase( X, 8 )
  if len(X32) == 3 and len(X16) == 3 and X32[1] == 'D' and \
     X16[1] == 'A' and X8[-1] == '5':
    print( X )