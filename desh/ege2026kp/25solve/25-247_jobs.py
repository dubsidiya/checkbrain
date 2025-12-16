# Автор: Е. Джобс

gen = ((x, sum(map(int, str(x))))
        for x in range(700_001, 1_000_000)
        if x % 13 == 0
            for s in (str(x), )
            if not ((s[-4] == '0' and s[-1]=='3') or
               (s[-5] == '0' and s[-2] == '3') or
               (s[-4] == '4' and s[-1] == '2') or
               '1' in s)
            )
for _ in range(5):
    print(*next(gen))
