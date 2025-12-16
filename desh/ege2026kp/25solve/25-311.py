# Автор: Е. Джобс

def ds(n):
    dd = set()
    for d in range(1, int(n**.5)+1):
        if n % d == 0:
            if str(d)[0] == '4':
                dd.add(d)
            if str(n // d)[0] == '4':
                dd.add(n // d)
    if len(dd) == 24:
        return max(dd)
    return 0

for x in range(10**6):
    if ds(x) > 0:
        print(x, ds(x))

