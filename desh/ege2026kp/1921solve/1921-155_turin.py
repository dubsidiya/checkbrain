# Автор: П. Тюрин

from itertools import *
from functools import *

@lru_cache(maxsize=None)
def f(n,m):
    if n+m>7: return 0
    if n+m<=7:
        events=[f(n+1,m),f(n+2,m),f(n,m+1),f(n,m+2)]
        if min(events)>0: return -max(events)
        if min(events)<=0: return -max(exp for exp in events if exp<=0)+1

#19 количество ситуаций, когда за один ход выигрывает Валера за 1 ход, после ошибки Паши
k=0
a = []
for n,m in product(range(10,-1,-1),repeat=2):
    events=[f(n+1,m),f(n+2,m),f(n,m+1),f(n,m+2)]
    if 1 in events:
            k+=1
            a += [(n, m)]
print(k, sorted(a))

#20 наибольшее и наименьшее значение n+m, когда выигрывает за три хода Паша
ans=[]
for n,m in product(range(10,-1,-1),repeat=2):
        if f(n,m)==3:
            ans.append(n+m)
print(min(ans),max(ans))

#21 количество всех ситуаций, когда выигрывает Валера
k=0
a = []
for n,m in product(range(10,-1,-1),repeat=2):
        if f(n,m)<0:
            k+=1
            a += [(n,m)]
print(k, sorted(a))