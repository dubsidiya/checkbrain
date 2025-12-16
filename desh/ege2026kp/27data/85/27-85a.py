# Автор: В. Лашин

from math import dist

clasters = []
for point in open('27-85a.txt'):
    point = list(map(float, point.replace(',', '.').split()))
    clasters.append([point])
    for claster in clasters[:-1]:
        if any(dist(point, claster_point) < 1 for claster_point in claster):
            clasters[-1] += claster
            clasters.remove(claster)


def extreme_point(claster_1, claster_2):
    distances = []
    for point_1 in claster_1:
        for point_2 in claster_2:
            distances.append([dist(point_1, point_2), [point_1, point_2]])
    return min(distances)[1]


extreme_points = [extreme_point(clasters[0], clasters[1])]
#print(len(clasters))
print(abs(int(sum(p1[0] + p2[0] for p1, p2 in extreme_points) / (2 * len(extreme_points)) * 10000)), end=' ')
print(abs(int(sum(p1[1] + p2[1] for p1, p2 in extreme_points) / (2 * len(extreme_points)) * 10000)))