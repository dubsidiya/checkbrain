# Автор: А. Кабанов
def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

results = []
for x in range(9_500_001,9_510_000):
    d = [i for i in div(x) if len(div(i))==0]
    F = sum(d)//len(d) if len(d)>0 else 0
    if F!=0 and F%813==0:
        results.append( (x,F) )
        if len(results)==5: break

for x,F in sorted(results, key = lambda p: p[1] ):
   print( x, F )