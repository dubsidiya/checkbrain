# Автор: PRO100 ЕГЭ

f = open('27-163b.txt')
n, k = map(int, f.readline().split())

otv = -1
max_pref = ['*'] * (k + 1)
min_pref = ['*'] * (k + 1)

a = []
for s in f:
    typ, value = [int(x) for x in s.split()]
    a.append([typ, value])

for i in range(k, n):
    # update pref
    if max_pref[a[i - k][0]] == '*':
        max_pref[a[i - k][0]] = a[i - k][1]
        min_pref[a[i - k][0]] = a[i - k][1]
    else:
        max_pref[a[i - k][0]] = max(max_pref[a[i - k][0]], a[i - k][1])
        min_pref[a[i - k][0]] = min(min_pref[a[i - k][0]], a[i - k][1])

    # update otv
    if max_pref[a[i][0]] != '*':
        otv = max(otv, abs(max_pref[a[i][0]] - a[i][1]))
        otv = max(otv, abs(min_pref[a[i][0]] - a[i][1]))

print(otv)
f.close()