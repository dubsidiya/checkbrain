# Mufazzalov
from fnmatch import fnmatch
from math import ceil, log
from itertools import product


def f(x):  # проверка требований к числу
    nn = int(x, 2)
    if nn < mm:
        if (o := oct(nn)[2:]) == o[::-1]:
            if fnmatch(str(nn), pattern):
                a[nn] = sum(map(int, o))


pattern = '*2023*'  # маска
h = '01'  # все возможные цифры
mm = 2023 ** 3 * 50  # правая граница диапазона поиска
km = (ceil(log(mm, 2)) - 2) // 2  # максимальная длина отраженной части (края)
a = {}  # найденные числа
for k in range(km + 1):  # длина одного края
    for i in product(h, repeat=k):  # генерация цифр края без первой цифры
        b = '1' + ''.join(i)  # один край
        for m in h:  # cередина, в том числе нулевая
            s = b + m + b[::-1]  # палиндром c серединой и с краями
            f(s)
        s = b + b[::-1]  # палиндром без середины
        f(s)
for i in sorted(a):
    print(i, a[i])
