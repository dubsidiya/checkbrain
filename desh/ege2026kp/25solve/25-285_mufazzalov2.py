from fnmatch import *


def check(n, m):
    d = '0123456789' + ''.join(sorted(list('qwertyuioplkjhgfdsazxcvbnm')))
    s = ''
    while n:
        s = d[n % m] + s
        n //= m
    return s == s[::-1]


for a in range(2023, 2023 ** 2 + 1, 100):
    if fnmatch(str(a), '20*23'):
        r = []
        for q in range(2, 37):
            if check(a, q):
                r.append(q)
        if len(r) >1:
            print(a, sum(r))
