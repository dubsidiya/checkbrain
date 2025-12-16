# Автор: А. Сражаев

def fact(n,p=2):
    for i in range(p,int(n**0.5)+1):
        if n % i == 0: return [i] + fact(n//i,i)
    return [n]

k = 0
for n in range(700_001,10**10):
    d = fact(n)
    if len(set(d)) == 1 and len(d) > 1:
        print(n,d[0])
        k+=1
    if k == 5: break