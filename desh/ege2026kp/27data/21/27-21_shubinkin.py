def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def read_a() -> tuple[list[tuple[float, float]], list[tuple[float, float]]]:
    with open('27-21a.txt') as f:
        f.readline()
        first = []
        second = []
        for line in f.readlines():
            x, y = map(float, line.replace(',', '.').split())
            if x > 5:
                first.append((x, y))
            elif y < 5:
                second.append((x, y))
    return first, second


def solve_a(first: list[tuple[float, float]], second: list[tuple[float, float]]) -> tuple[float, float]:
    dmin = 10**9
    dmax = 0
    for x1, y1 in first:
        for x2, y2 in second:
            d = distance(x1, y1, x2, y2)
            if d < dmin:
                dmin = d
                min_dots = x1, y1, x2, y2
            if d > dmax:
                dmax = d
                max_dots = x1, y1, x2, y2
    return dmin, dmax


dmin_a, dmax_a = solve_a(*read_a())
print('Ответ А:', int(dmin_a * 10000), int(dmax_a * 10000))


def read_b() -> tuple[list[tuple[float, float]], list[tuple[float, float]], list[tuple[float, float]]]:
    with open('27-21b.txt') as f:
        f.readline()
        first = []
        second = []
        third = []
        for line in f.readlines():
            x, y = map(float, line.replace(',', '.').split())
            if 7.5 < x < 10.5 and 2.5 < y < 6.5:
                first.append((x, y))
            elif x < 5 and y > 5:
                second.append((x, y))
            elif 1.5 < x < 5.5 and 1.5 < y < 4.5:
                third.append((x, y))
    return first, second, third


def solve_b(first, second, third):
    dmin12, dmax12 = solve_a(first, second)
    dmin13, dmax13 = solve_a(first, third)
    dmin23, dmax23 = solve_a(second, third)
    return min(dmin12, dmin13, dmin23), max(dmax12, dmax13, dmax23)


dmin_b, dmax_b = solve_b(*read_b())
print('Ответ Б:', int(dmin_b * 10000), int(dmax_b * 10000))
