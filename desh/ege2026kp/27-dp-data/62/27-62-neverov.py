# Автор: А. Неверов

f = open("27-62b.txt")
n = int(f.readline())
a = [int(x) for x in f]
a.sort()
m = set(a)
mx = 0
for i in range(n):
    for d in range(1, 101):
        cur = a[i]
        k = 1
        while cur + d in m:
            k += 1
            mx = max(mx, k)
            cur += d
print(mx)