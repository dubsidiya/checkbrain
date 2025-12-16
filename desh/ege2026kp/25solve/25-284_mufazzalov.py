# Mufazzalov
from fnmatch import fnmatch
from math import ceil, log
from itertools import product

def f(x, y):  # проверка требований к числу
    nn = d = int(x, y)
    if nn < mm:
        if fnmatch(str(nn), pattern):
            r7 = []
            while d:
                r7.append(d % 7)
                d //= 7
            if r7 == r7[::-1]:
                a[nn] = sum(map(int, oct(nn)[2:]))


pattern = '*2*0'  # маска
t = '012'  # все возможные цифры
mm = 2023 ** 3  # правая граница диапазона поиска
bas = 3
km = (ceil(log(mm, bas)) - 2) // 2  # максимальная длина отраженной части (края)
# записи числа в каждой системе счисления

a = {}  # найденные числа
for e in t[1:]:  # допустимая первая цифра
    f(e, bas)  # палиндром с ненулевой серединой без краев
    for k in range(km + 1):  # длина одного края
        for i in product(t, repeat=k):  # генерация края без первой цифры
            b = e + ''.join(i)  # один край
            for m in t:  # cередина, в том числе нулевая
                s = b + m + b[::-1]  # палиндром c серединой и с краями
                f(s, bas)
            s = b + b[::-1]  # палиндром без середины
            f(s, bas)
for i in sorted(a):
    print(i, a[i])
