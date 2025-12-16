from string import ascii_uppercase, digits

A21 = (digits + ascii_uppercase)[:21]

for x in A21:
  n = int( f"912{x}8745", 21) + int( f"791{x}065", 21)
  if n % 20 == 0:
    print( n // 20 )
