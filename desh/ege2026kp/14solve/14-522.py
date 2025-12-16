n = 77*81**2031 + 23*729**1037 - 7*9**3023
b = 81

count = 0
while n:
  if n % b % 4 == 0:
    count += 1
  n //= b

print( count )

