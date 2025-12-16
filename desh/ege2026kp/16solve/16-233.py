from timeit import default_timer

t0 = default_timer()
F = list(range(17))
LIMIT = int('123456032', 7)
n = 16
count = 14
while True:
  F[n] = F[n-2] + n + 3
  if F[n] > LIMIT: break
  count += 1
  n += 2
  F.extend( [0, 0] )
print( count, default_timer()-t0 )

# Автор: О. Лысенков

from functools import  cache
@cache
def f(n):
    if n < 15:
        return n
    elif n % 2 == 0 and n >= 15:
        return f(n-2) + n + 3
    elif n % 2 != 0 and n >= 15:
        return float('inf')
t0 = default_timer()
k = 0
for i in range(1,10000000):
    if  f(i) < int('123456032',7):
        k += 1
print(k, default_timer()-t0)