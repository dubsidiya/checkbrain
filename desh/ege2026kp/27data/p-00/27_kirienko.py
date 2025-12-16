import random
import math


def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Количество кластеров
K = 3

# Имя файла с данными
f = open("27-p00b.txt")
f.readline()
P = []
for line in f:
    x, y = line.replace(",", ".").split()
    P.append((float(x), float(y)))

n = len(P)

# Выбираем случайные точки
c = [random.choice(P) for i in range(K)]

# Ищем начальные центры кластеров, как три точки, максимально удалённых
for j in range(K):
    for i in range(n):
        s1 = 0
        s2 = 0
        for jj in range(K):
            if jj != j:
                s1 += dist(c[j], c[jj])
                s2 += dist(P[i], c[jj])
        if s2 > s1:
            c[j] = P[i]

group = [0] * n

# Строим разбиение на кластеры, пока происходят изменения
count = n
while count:
    count = 0
    for i in range(n):
        grp = group[i]
        for j in range(K):
            if dist(P[i], c[j]) < dist(P[i], c[grp]):
                grp = j
        if grp != group[i]:
            count += 1
            group[i] = grp

    # Теперь пересчитываем центры кластеров
    for j in range(K):
        sx = 0
        sy = 0
        sn = 0
        for i in range(n):
            if group[i] == j:
                sx += P[i][0]
                sy += P[i][1]
                sn += 1
        if sn:
            c[j] = (sx / sn, sy / sn)
    print(f"Закончена итерация, выполнено {count} изменений")
    print(f"Новые центры: {c}")

# Теперь ищем центры кластеров в соответствии с условием задачи
for j in range(K):
    best_sum = float("inf")
    idx = [i for i in range(n) if group[i] == j]
    for i1 in idx:
        s = 0
        for i2 in idx:
            s += dist(P[i1], P[i2])
        if s < best_sum:
            c[j] = P[i1]
            best_sum = s
print(f"Окончательные центры: {c}")
print("Ответ: ")
for i in range(2):
    s = 0
    for j in range(K):
        s += c[j][i]
    s /= K
    s *= 10000
    print(int(s))