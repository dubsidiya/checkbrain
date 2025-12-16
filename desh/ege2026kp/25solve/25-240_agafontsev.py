# Автор: А. Агафонцев

def sdivs(n):
    d = 1
    s = 0
    while d*d < n:
        if n%d == 0:
            s += d + n//d
        d += 1
    if d*d == n:
        s += d
    return s

k = 0
for i in range(10**7, 0, -1):
    s = str(i)
    if s[0]+s[-1]=='97' and '55' in s[2:]:
        print(i, sdivs(i)%21)
        k += 1
        if k == 5:
            break