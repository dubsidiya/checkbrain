# Mufazzalov
from fnmatch import fnmatch
from math import ceil, log
from itertools import product


def f(x, y):  # проверка требований к числу
    nn = int(x, y)
    if nn < mm:
        if fnmatch(str(nn), pattern):
            a[nn] = a.get(nn, []) + [y]


pattern = '20*23'  # маска
h = '0123456789abcdefghijklmnopqrstuvwxyz'  # все возможные цифры
mm = 2023 ** 2  # правая граница диапазона поиска
zz = list(range(2, 37)) # основания систем счисления
lz = len(zz)  # количество систем счисления
km = {}  # максимальная длина отраженной части (края)
# записи числа в каждой системе счисления
for base in zz:
    km[base] = (ceil(log(mm, base)) - 2) // 2
a = {}  # найденные числа
for bas in zz:  # цикл по системам счисления
    t = h[:bas]  # цифры в данной системе счисления
    for e in t[1:]:  # допустимая первая цифра
        f(e, bas)  # палиндром с ненулевой серединой без краев
        for k in range(km[bas] + 1):  # длина одного края
            for i in product(t, repeat=k):  # генерация цифр края без первой цифры
                b = e + ''.join(i)  # один край
                for m in t:  # cередина, в том числе нулевая
                    s = b + m + b[::-1]  # палиндром c серединой и с краями
                    f(s, bas)
                s = b + b[::-1]  # палиндром без середины
                f(s, bas)

for i in sorted(a):
    if len(a[i]) > 1:
        print(i, sum(a[i]))
