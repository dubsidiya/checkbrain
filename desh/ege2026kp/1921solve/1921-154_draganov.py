#154 Драганов Андрей Викторович, две динамики
from functools import *

#опишем все ходы из позиции p (отфильтруем допустимые)
def H(p): return [h for h in [p-3, p-5, (p+1)//2] if h>=0 and h!=p]

# функция возвращает W, если позиция p выигрышная, а иначе  - L.
@lru_cache(None)
def f(p):
  if p<6: return 'L' if p%2==1 else 'W'
  return 'W' if any(f(h)=='L' for h in H(p)) else 'L'

# функция возвращает количество ходов до конца игры в самой длинной ветке стратегии
@lru_cache(None)
def c(p):
  if p<6: return 0
  if f(p)=='L': return 1 + max(c(h) for h in H(p))
  return 1 + min(c(h) for h in H(p) if f(h)=='L')

S = range(6,1000) #Это список рассматриваемых позиций (с запасом)
a19 = [p for p in S if f(p)=='W' and c(p) in [3,4]]
a20 = [p for p in S if f(p)=='L' and c(p) in [4,5]]
a21 = [p for p in S if f(p)=='W' and any(c(h)==1 and f(h)=='W' for h in H(p))]
print('19', a19[-1], a19)
print('20', a20[:2], a20)
print('21', a21[0], a21)

