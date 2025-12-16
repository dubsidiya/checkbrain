n = 30*36**231 + 18*6**101 - 3*36**45 - 2357
b = 36

count = 0
while n:
  d = n % b
  if (d % 5 == 0 or d % 3 == 0) and d % 15 != 0:
    count += 1
  n //= b

print( count )

