from sys import setrecursionlimit

F = [0] * 48000
for n in range(20):
  F[n] = n

for n in range(20,47873):
  F[n] = (n-6)*F[n-7]

print( (F[47872] - 290*F[47865]) / F[47858] )

# Автор А. Кабанов

from functools import cache
@cache
def F( n ):
  return n if n < 20 else \
         (n-6)*F(n-7)

for n in range(47873): F(n)

print( (F(47872) - 290*F(47865)) / F(47858) )
