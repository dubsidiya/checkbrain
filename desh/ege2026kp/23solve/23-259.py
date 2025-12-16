N = 10000
count = 0
blocked, node = 3000, 5000
for _ in range(2):
  f = [0]*(N+1)
  f[1] = 1
  limit = 0
  for i in range(2,10001):
    if i == blocked: f[i] = 0
    else:
      f[i] = 0
      if i - 3 >= limit: f[i] += f[i-3]
      if i - 5 >= limit: f[i] += f[i-5]
      if i % 2 == 0 and i // 2 >= limit: f[i] += f[i//2]
      if i == node: limit = node
  count += f[N] % 10**6
  blocked, node = node, blocked

print( count % 10**6 )
