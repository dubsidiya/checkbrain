def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def get_centr_coords(coords: list[tuple[float, float]]) -> tuple[float, float]:
    min_sum = float('inf')
    x_c = y_c = 0
    for x, y in coords:
        cur_sum = sum(map(lambda cs: distance(x, y, *cs), coords))
        if cur_sum < min_sum:
            min_sum = cur_sum
            x_c, y_c = x, y
    return x_c, y_c


def solve_a():
    with open('27-22a.txt') as f:
        f.readline()  # пропускаем первую строку (заголовок)
        first = []
        second = []
        for line in f.readlines():
            x, y = map(float, line.replace(',', '.').split())
            if -3 <= x <= 0 and 1 <= y <= 4:
                first.append((x, y))
            if 1 <= x <= 3 and -2 <= y <= 0:
                second.append((x, y))
    x_c_1, y_c_1 = get_centr_coords(first)
    x_c_2, y_c_2 = get_centr_coords(second)
    print(f'Координаты первого центра: {x_c_1}, {y_c_1}')
    print(f'Координаты второго центра: {x_c_2}, {y_c_2}')
    px = (x_c_1 + x_c_2) / 2
    py = (y_c_1 + y_c_2) / 2
    print(int(px * 100_000), int(py * 100_000))


def solve_b():
    with open('27-22b.txt') as f:
        f.readline()  # пропускаем первую строку (заголовок)
        first = []
        second = []
        third = []
        for line in f.readlines():
            x, y = map(float, line.replace(',', '.').split())
            if -3 <= x <= -1 and -3 <= y <= 0:
                first.append((x, y))
            if -1 <= x <= 3 and 2 <= y <= 4:
                second.append((x, y))
            #if 1 <= x <= 5 and -3 <= y <= 1:
            if 0.5 <= x and -3.5 <= y <= 1.5:
                third.append((x, y))
    x_c_1, y_c_1 = get_centr_coords(first)
    x_c_2, y_c_2 = get_centr_coords(second)
    x_c_3, y_c_3 = get_centr_coords(third)
    print(f'Координаты первого центра: {x_c_1}, {y_c_1}')
    print(f'Координаты второго центра: {x_c_2}, {y_c_2}')
    print(f'Координаты третьего центра: {x_c_3}, {y_c_3}')
    px = (x_c_1 + x_c_2 + x_c_3) / 3
    py = (y_c_1 + y_c_2 + y_c_3) / 3
    print(int(px * 100_000), int(py * 100_000))


solve_a()
solve_b()
