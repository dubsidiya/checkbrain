# Автор: Д. Статный

from math import gcd

def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d |= {i, x//i}
    return sorted(d)

def p(m):
    u = div(m)
    if len(div(m))>=7:
        return gcd(u[0], u[1])==1 and gcd(u[0], u[2])==1 and gcd(u[1], u[2])==1 and gcd(u[0], u[3])==1 \
               and gcd(u[1], u[3])==1 and gcd(u[2], u[3])==1 and gcd(u[0], u[4])==1 and gcd(u[1], u[4])==1 and \
               gcd(u[2], u[4])==1 and gcd(u[3], u[4])==1 and gcd(u[0], u[5])==1 and gcd(u[0], u[5])==1 \
               and gcd(u[1], u[5])==1 and gcd(u[2], u[5])==1 and gcd(u[3], u[5])==1 and gcd(u[4], u[5])==1
    else:
        return False

count = 0
ans = []
for i in range(999_999_999, 100_000_000, -2):
    if p(i):
        ans.append([i, div(i)[-1]])
        count += 1
    if count==5:
        break
for x in sorted(ans):
    print(x[0], x[1])
