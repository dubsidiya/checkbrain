# Автор: А. Кабанов
def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

k = 0
for x in range(23_600_001,23_601_000):
    d = [i for i in div(x) if len(div(i))==0]
    M = d[0]+d[-1] if len(d)>0 else 0
    if M%213==171:
        print(x,M)
        k += 1
        if k==6: break