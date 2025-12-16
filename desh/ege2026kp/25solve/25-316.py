# Автор: Е. Джобс

from fnmatch import fnmatch
for x in range(2468035, 10**9, 100):
    if x % 13 == 0 and fnmatch(str(x), '24*68?35'):
        s = str(x)
        if s[-3] in '39' and all(c in '02468' for c in s[2:-5]):
            print(x, x // 13)

print('--')
for c in '39':
    x = int('2468' + c + '35')
    if x % 13 == 0:
        print(x, x//13)

for b in '02468':
    for c in '39':
        x = int('24' + b + '68' + c + '35')
        if x % 13 == 0:
            print(x, x//13)

for a in '02468':
    for b in '02468':
        for c in '39':
            x = int('24' + a + b + '68' + c + '35')
            if x % 13 == 0:
                print(x, x//13)
