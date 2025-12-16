# Автор: В. Лашин

def pr_m(x, p = 2):
    for d in range(p, int(x**0.5) + 1):
        if x % d == 0:
            return [d] + pr_m(x//d, d)
    return [x]

count = 0
for x in range(24_517_512 + 1, 10**9):
    if len(pr_m(x)) == 12:
        print(x, max(pr_m(x)))
        count += 1
        if count == 5: break
