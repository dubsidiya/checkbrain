# Автор: А. Минак

def f(s, e):
    if s > e:
        return 0
    if s == e:
        return 1

    p = int(str(s)[-1])
    b = int(str(s)[0])
    r = [1, p, b]

    q = 0
    for x in set(r):
        if x != 0:
            q += f(s+x, e)
    return q

print(f(82, 95)*f(95,103)*f(103,124))


