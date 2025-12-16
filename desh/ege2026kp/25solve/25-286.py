from fnmatch import fnmatch

step = 2023*6*19  # 2023 не делится на 2, 3 и 19!
start = 200000000 // step * step

results = []
count = 0
n = start
while count < 5:
  if fnmatch( str(n), "1*1*1?" ):
    results += [n]
    count += 1
  n -= step

for n in results[::-1]:
  print( n, n // 2023 )