# Автор: Д. Статный

count = 0
for s in open('9-182.csv'):
    a = [int(x) for x in s.split(';')]
    if a[0]!=0 and a[1]**2-4*a[0]*a[2]>0:
        count += 1
print(count)
