# Автор: А. Кабанов
def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

k = 0
for x in range(32_500_001,32_501_000):
    d = [i for i in div(x) if len(div(i))==0]
    S = sum(d)
    if S!=0 and S%145==0:
        print(x,S)
        k += 1
        if k==7: break
