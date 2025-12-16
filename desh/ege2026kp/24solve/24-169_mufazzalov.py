# Автор: Д. Муфаззалов

r = 'XYZ'
m = n = 0
for s in 'XXYZ': #open('24-169.txt').readline():
    if s == r[m % 3]:
        m += 1
        n = max(m, n)
    else:
        m = (s == r[0])
print(n - n % 3)