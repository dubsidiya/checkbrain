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
            if ispalindrom(x, 25):
                a[nn] = sum(map(int, oct(nn)[2:]))


pattern = '*2*02*3*'  # маска
t = '01234'  # все возможные цифры
mm = 10 * 2023 ** 3  # правая граница диапазона
zz = sorted([5, 25])  # основания систем счисления
bas = 5  # основная система счисления
le = {i: int(log(i, bas)) for i in zz[1:]}
lz = len(zz)  # количество систем счисления
km = (ceil(log(mm, bas)) - 2) // 2  # максимальная длина отраженной части (края)
a = {}  # найденные числа
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
    print(i, a[i])
