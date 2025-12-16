# Автор: И. Карпачёв

def f(x, y):
    A = 6 <= x <= 52
    B = 153 % x == 0 and x not in [1, 153]
    C = y % x == 0 and x not in [1, y]
    return C and (A <= B)

for y in range(1, 10000):
    D = [e for e in range(2, y) if y % e == 0]
    if D and all(f(x, y) == 0 for x in range(1, 10000)):
        print(y)
