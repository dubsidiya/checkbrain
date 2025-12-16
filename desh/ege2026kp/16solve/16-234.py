from timeit import default_timer

LIMIT = 132567821562

t0 = default_timer()
F = [0]*6
G = [0]*6
for i in range(1,5):
  F[i] = (i+1)*i
  G[i] = (-i+1)*(-i)

count = 9

n = 5
while True:
  F[n] = F[n-5] + 2*n + 2356
  if abs(F[n]) > LIMIT: break
  count += 1
  n += 5
  F.extend( [0, 0, 0, 0, 0] )

n = -5
while True:
  if n % 5 != 0:
    G[(-n)] = G[-(n+5)] + 7*n
    if abs(G[-n]) > LIMIT: break
    count += 1
  n -= 1
  G.append( 0 )

print( count, default_timer()-t0 )


# Автор: О. Лысенков

from functools import  cache
@cache
def f(n):
    if -5 < n < 5: return (n + 1) * n
    elif  n % 5 == 0:
        if n >= 5:
            return f(n - 5) + 2 * n + 2356
        else:
            return float('inf')
    else:
        if n >= 5:
            return float('inf')
        else:
            return f(n + 5) + 7 * n

t0 = default_timer()

k = 0
for i in range(1,  10 ** 6):
    if abs(f(i)) < LIMIT:
        k += 1
for i in range(0, -10 ** 6,-1):
    if abs(f(i)) < LIMIT:
        k += 1

print(k, default_timer()-t0)