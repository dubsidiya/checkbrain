# Автор: В. Лашин

from math import dist
 
clasters = []
eps = 1
for point in open('27-87a.txt'):
    point = list(map(float, point.replace(',', '.').split()))
    clasters.append([point])
    for claster in clasters[:-1]:
        if any(dist(point, claster_point) < eps for claster_point in claster):
            clasters[-1] += claster
            clasters.remove(claster)
 
 
def centroid(claster):
    sum_x = sum_y = 0
    for x, y in claster:
        sum_x += x
        sum_y += y
    average_x = sum_x / len(claster)
    average_y = sum_y / len(claster)
    return [average_x, average_y]
 
 
centroids = [centroid(claster) for claster in clasters]
# print(len(clasters))
print(abs(int(sum(x for x, y in centroids) / len(centroids) * 10000)), end=' ')
print(abs(int(sum(y for x, y in centroids) / len(centroids) * 10000)))