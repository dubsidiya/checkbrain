# Автор: П. Тюрин

from itertools import *
from functools import *

@lru_cache(maxsize=None)
def f(n,m):
    if n+m<2: return 0
    if n+m>=2 and n>=0 and m>=0:
        events=[]
        if n>=1: events=events+[f(n-1,m)]
        if n>=2: events=events+[f(n-2,m)]
        if m>=1: events=events+[f(n,m-1)]
        if m>=2: events=events+[f(n,m-2)]
        if min(events)>0: return -max(events)
        if min(events)<=0: return -max(exp for exp in events if exp<=0)+1

#19 за один ход выигрывает Валера, после ошибки Паши, максимальное значение
ans=[]
for n,m in product(range(8,0,-1),repeat=2):
    events=[]
    if n>=1: events=events+[f(n-1,m)]
    if n>=2: events=events+[f(n-2,m)]
    if m>=1: events=events+[f(n,m-1)]
    if m>=2: events=events+[f(n,m-2)]
    if 1 in events:#игрок мог совершить ошибку и отправить в 1
            ans.append(n+m)
print(max(ans))

#20 наибольшее и наименьшее значение n+m, когда выигрывает за три хода Паша, но не может гарантированно выиграть за два хода
ans=[]
b = []
for n,m in product(range(8,0,-1),repeat=2):
        if f(n,m)==3:
            ans.append(n+m)
            b.append( (n,m) )
print(min(ans),max(ans), sorted(b) )

#21 количество всех состояний игры, когда выигрывает Валера
ans=[]
for n,m in product(range(8,0,-1),repeat=2):
        if f(n,m)<0 and n+m >= 3:
            ans.append((n,m))
print(len(ans), sorted(ans))
