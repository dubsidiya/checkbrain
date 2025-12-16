n = 39*121**319 + 46*11**913 - 15*1331**15 - 1993
b = 121

count = 0
while n:
  if 64 <= n % b <= 104:
    count += 1
  n //= b

print( count )

