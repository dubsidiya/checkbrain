# Автор: В. Лашин

def f(now, end):
    if now == end:
        return 1
    if now > end + 10 or now % 3 == 0:
        return 0
    return f(now - 1, end) + f(now + 3, end) + f(now * 2, end)

print(f(5, 100))
