n = 15*49**237 + 37*343**500 - 14*7**35
b = 49

count = 0
while n:
  if n % b > 15:
    count += 1
  n //= b

print( count )

