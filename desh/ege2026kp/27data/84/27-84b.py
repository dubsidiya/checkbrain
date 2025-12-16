# Автор: В. Лашин

from math import *
 
def d(claster):
    mx = 0
    points = []
    for point1 in claster:
        for point2 in claster:
            if dist(point1, point2) > mx:
                mx = dist(point1, point2)
                points = [point1, point2]
    return points
 
 
clasters = []
for point in open('27-84b.txt'):
    point = list(map(float, point.replace(',', '.').split()))
    clasters.append([point])
    for claster in clasters[:-1]:
        if any(dist(point, point_claster) < 1 for point_claster in claster):
            clasters[-1] += claster
            clasters.remove(claster)
ds = [d(claster) for claster in clasters]
# print(len(ds)) проверка правильности выделения кластеров
print(abs(int(sum(opor[0][0] + opor[1][0] for opor in ds) / (len(ds) * 2) * 10000)), end=' ')
print(abs(int(sum(opor[0][1] + opor[1][1] for opor in ds) / (len(ds) * 2) * 10000)))