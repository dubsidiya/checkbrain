# Автор: А. Бычков

Fib = [1, 1]

while Fib[-1] < 100:
    Fib += [Fib[-2] + Fib[-1]]

First = [''] + [str(i) for i in range(10)]

ans = []

for x1 in First:
    for x2 in set(Fib[:-1]):
        for x3 in set(Fib[:-1]):
            x = int(f'73{x1}5{x2}486{x3}')
            if x%43== 0 and x <= 10**9:
                ans += [x]

for num in sorted(set(ans)):
    print(num , num // 43)