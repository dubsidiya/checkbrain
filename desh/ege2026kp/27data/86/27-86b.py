# Автор: В. Лашин

from math import dist
 
clasters = []
eps = 1
for point in open('27-86b.txt'):
    point = list(map(float, point.replace(',', '.').split()))
    clasters.append([point])
    for claster in clasters[:-1]:
        if any(dist(point, claster_point) < eps for claster_point in claster):
            clasters[-1] += claster
            clasters.remove(claster)
 
 
def mediana_x(claster):
    for point_1 in claster:
        count = 0
        for point_2 in claster:
            if point_2[0] > point_1[0]:
                count += 1
        if count == len(claster) // 2:
            return point_1[0]
 
 
def mediana_y(claster):
    for point_1 in claster:
        count = 0
        for point_2 in claster:
            if point_2[1] > point_1[1]:
                count += 1
        if count == len(claster) // 2:
            return point_1[1]
 
 
medians_x = [mediana_x(claster) for claster in clasters]
medians_y = [mediana_y(claster) for claster in clasters]
#print(len(clasters))
print(abs(int(sum(medians_x) / len(medians_x) * 10000)), end=' ')
print(abs(int(sum(medians_y) / len(medians_y) * 10000)))