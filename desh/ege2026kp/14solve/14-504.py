from string import digits, ascii_uppercase

A = digits + ascii_uppercase

for x in A[:22]:
  n = int( f'A23{x}AC0', 22 ) + int( f'GB{x}21670', 22 )
  if n % 21 == 0:
    print( x, n // 22 )