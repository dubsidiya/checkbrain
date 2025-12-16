n = 17*125**453 + 117*5**231 - 3*5**13 - 2357
b = 125

count = 0
while n:
  if n % b <= 37:
    count += 1
  n //= b

print( count )

