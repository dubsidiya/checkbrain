# Автор: А. Агафонцев

a = 65001
k = 0
while k != 7:
    s =  str(a)
    if s[0]=='6' and '97' in s and s[-2] == '5' :
        m = 0
        d = 1
        sm = 0
        while d * d < a:
            if a % d == 0:
                if d % 2 == 0:
                    sm += d
                    m += 1

                if (a//d)% 2 == 0:
                    sm += a//d
                    m += 1
            d += 1
        if d * d == a and d % 2 == 0:
            sm += d
            m += 1

        if m >= 4:
            print(a, sm)
            k += 1
    a += 1