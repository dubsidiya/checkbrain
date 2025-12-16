# Mufazzalov
from fnmatch import fnmatch
from math import ceil, log
from itertools import product


def ispalindrom(x, y):
    # проверка на палиндром в остальных системах счисления
    tl = le[y]
    x = '0' * ((tl - len(x) % tl) % tl) + x
    xi = [x[i:i + tl] for i in range(0, len(x), tl)]
    return xi == xi[::-1]


def f(x):  # проверка
    nn = int(x, bas)
    if nn < mm:  # проверка на вхождение в диапазон
        if fnmatch(str(nn), pattern):  # проверка на маску
            a[nn] = 1
            for u in zz[1:]:  # цикл по другим системам счисления
                if ispalindrom(x, u):
                    a[nn] += 1


pattern = '*2??3*'  # маска
t = '012'  # все возможные цифры
mm = 10 * 2023 ** 3  # правая граница диапазона
zz = sorted([3, 9, 27])  # основания систем счисления
bas = 3  # основная система счисления
le = {i: int(log(i, bas)) for i in zz[1:]}
lz = len(zz)  # количество систем счисления
km = (ceil(log(mm, bas)) - 2) // 2  # максимальная длина отраженной части (края)
a = {}  # найденные числа с количество систем счисления
  # цифры в данной системе счисления
for e in t[1:]:  # допустимая первая цифра
    f(e)  # палиндром с ненулевой серединой без краев
    for k in range(km + 1):  # длина одного края
        for i in product(t, repeat=k):  # генерация края без первой цифры
            b = e + ''.join(i)  # один край
            for m in t:  # cередина, в том числе нулевая
                s = b + m + b[::-1]  # палиндром c серединой и с краями
                f(s)
            s = b + b[::-1]  # палиндром без середины
            f(s)
for i in sorted(a):
    if a[i] == lz:
        print(i, sum(map(int, oct(i)[2:])))
