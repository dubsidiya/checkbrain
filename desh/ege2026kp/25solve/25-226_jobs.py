# Автор: Е. Джобс

from itertools import combinations, product
f_star = [['']]
s_star = [['']]
for i in range(1, 4):
    f_star += list(combinations('234', r=i))
    s_star += list(combinations('678', r=i))

res = set()
for a, b in product(f_star, s_star):
    x = int('1' + ''.join(a) + '5' + ''.join(b) + '9')
    if x % 21 == 0:
        res.add(x)

for x in sorted(res):
    print(x, x // 21)
