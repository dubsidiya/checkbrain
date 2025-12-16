n = 20*3**243 + 17*81**70 + 14*243**35 + 254 - 224*3**30
b = 243

count = 0
while n:
  d = n % b
  if d in [2, 3, 5, 7, 11, 13, 17, 19]:
    count += 1
  n //= b

print( count )

