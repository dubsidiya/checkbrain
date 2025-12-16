N = 112500
coins = [1, 3, 5]

T = [ [1 for i in range(N+1)] ]

for c in coins[1:]:
  T.append( [1] + [0]*N )
  for n in range(1,N+1):
    T[-1][n] = T[-2][n] + T[-1][n-c]

count = T[-1][N]
print( count, sum( map(int, str(count)) ) )
#for i, c in enumerate(coins):
#  print( T[i][:10] )

#---------------------------------------------
# Автор: А. Игнатюк

from functools import cache
goal = 112500

@cache
def f(n, pred):
  if n == goal:
    return 1
  elif n > goal:
    return 0
  else:
    return sum( f(n+new_coin, new_coin) for new_coin in [1, 3, 5]
                if new_coin >= pred )

for n in range(goal, -1, -1):
  f(n, 0)

count =  f(0, 0)
print( count, sum( map(int, str(count)) ) )