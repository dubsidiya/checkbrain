# Автор: И. Карпачёв

def f(x, y):
    A = 6 <= x <= 46
    B = 161 % x == 0 and x not in [1, 161]
    C = y % x == 0 and x not in [1, y]
    return (not B and A) or not C

for y in range(1, 10000):
    D = [e for e in range(2, y) if y % e == 0]
    if D and all(f(x, y) for x in range(1, 10000)):
        print(y)
