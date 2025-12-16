# Автор: Кульпин Д.

o = open("26-57.txt")
k = 0
a, b = map(int, o.readline().split())
p = sorted([int(i) for i in o])

while True:
    j = 2#сколько деталей в сварке

    while sum(p[-j:]) < b:#пока сумма сварок меньше 20000
        j+=1
        if j == len(p): break
    if j == len(p): break
    z = sum(p[-j+1:])# чтобы уменьшить кол-во сварок берем на один провод меньше,чем j
    l = min([int(x) for x in p if x >= b - z])# выберем из оставшегося куска минимально подходящий
    provod = l + z# общая длина получившегося провода
    p = p[:1-j]# отрезаем использованную часть
    ind = p.index(l)
    p = p[:ind] + p[ind+1:]# вырезаем минимально пододящий элемент
    if provod-b != 0: p.append(provod-b)# если провод чуть длиннее, отрез кладем в массив
    k+=(j-1)# количество сварок
    p = sorted(p)
print(k, len(p))

