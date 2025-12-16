# Автор: А. Кабанов
def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

results = []
for x in range(55_000_001,55_010_000):
    D = [i for i in div(x) if len(div(i))==0 and i%1000==777]
    if len(D)>0:
      results.append( (x,D[0]) )
      if len(results)==4: break

for x,F in sorted(results, key = lambda p: p[1] ):
   print( x, F )