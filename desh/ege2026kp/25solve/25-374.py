# Автор: В. Лашин

def f(d, n):
    for d in range(d, int(n**0.5)+1):
        if n % d == 0:
            return [d] + f(d, n//d)
    return [n]

k = 0
for x in range(13475124+1, 10**9):
    pm = f(2, x)
    if len(pm) == 5 and all('5' in str(d) for d in pm):
        print(x, max(pm))
        k += 1
        if k == 5: break
