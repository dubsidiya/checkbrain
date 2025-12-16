# Автор: Д. Статный

ans = []
for s in open('9-183.csv'):
    a = sorted([int(x) for x in s.split(';')])
    if a[2]<a[0]+a[1]:
        p = sum(a)/2
        s = (p*(p-a[0])*(p-a[1])*(p-a[2]))**0.5
        if int(s)==s:
            ans.append(s)
print(len(ans))

