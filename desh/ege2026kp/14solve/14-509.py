from string import ascii_uppercase, digits

A21 = (digits + ascii_uppercase)[:21]

for x in A21:
  n = int( f"82934{x}2", 21) + int( f"2924{x}{x}7", 21) \
       + int( f"67564{x}8", 21 )
  if n % 20 == 0:
    print( n // 20 )
    break