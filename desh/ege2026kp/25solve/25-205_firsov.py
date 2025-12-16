# Автор: М. Фирсов

from time import time
st = time()
#формирование полиндромов
var = [list(map(str, (range(10)))), [2*i for i in map(str, (range(10)))]]
for _ in range(7):
    var.append([i + j + i for i in var[0] for j in var[_]])
var = [int(j) for i in var for j in i if j[0] != "0"]

#умножение цифр в числе
def p(n):
    r = 1
    for i in str(n):
        if i in "01": continue
        r *= int(i)
    return r

#проверка на простые числа
a = []
for n in var[18:]:# 18: ислкючает числа [1:99]
    ok = True
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0: ok = False; break
    if ok: a.append(n)

#распределение на группы по произведению
s = {}
for i in a:
    pr = p(i)
    if pr in s:
        s[pr] += [i]
    else: s[pr] = [i]
s = s.values()
l = max(list(map(len, s)))

#вывод ответа
for i in s:
    if l == len(i):
        for j in (i[-5:]):
            print(j)
        break

print( "Время:", int(time() - st), "с" )