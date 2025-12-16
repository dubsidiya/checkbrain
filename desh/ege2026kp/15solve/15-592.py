# Автор: И. Карпачёв

def f(x, y):
    A = 4 <= x <= 82
    B = 211 % x == 0 and x not in [1, 211]
    C = y % x == 0 and x not in [1, y]
    return (B or not A) <= (not C)

res = []
for y in range(1, 10000):
    D = [e for e in range(2, y) if y % e == 0]
    if D and all(f(x, y) for x in range(1, 10000)):
        res.append([len(D), y])
        # print(y, D)

print(max(res))
