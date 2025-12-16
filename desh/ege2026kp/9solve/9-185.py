# Автор: Д. Статный

count = 0
for s in open('9-183.csv'):
    a = sorted([int(x) for x in s.split(';')])
    if a[2]<a[0]+a[1]:
        if a[0]**2 + a[1]**2 > a[2]**2:
            count += 1
print(count)


