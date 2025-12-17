# Автор: PRO100 ЕГЭ

f = open('27-164b.txt')
n, k = map(int, f.readline().split())

otv = -1
max_pref = ['*'] * 100_000
min_pref = ['*'] * 100_000

a = ['*' for _ in range(10**7 + 1)]
for s in f:
    typ, sek, value = [int(x) for x in s.split()]
    a[sek] = [typ, value]


for i in range(k, 10**7 + 1):
    # update pref
    if a[i - k] != '*':
        if max_pref[a[i - k][0]] == '*':
            max_pref[a[i - k][0]] = a[i - k][1]
        else:
            max_pref[a[i - k][0]] = max(max_pref[a[i - k][0]], a[i - k][1])

        if min_pref[a[i - k][0]] == '*':
            min_pref[a[i - k][0]] = a[i - k][1]
        else:
            min_pref[a[i - k][0]] = min(min_pref[a[i - k][0]], a[i - k][1])

    # update otv
    if a[i] != '*':
        if max_pref[a[i][0]] != '*':
            otv = max(otv, abs(max_pref[a[i][0]] - a[i][1]))
        if min_pref[a[i][0]] != '*':
            otv = max(otv, abs(min_pref[a[i][0]] - a[i][1]))


print(otv)
f.close()