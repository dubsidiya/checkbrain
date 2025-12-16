# Автор: А. Агафонцев

k = 0
for i in range (10**7-1, 0, -1):
    if i % 217 == 0:
        s = str(i)
        if s[0]+s[1]+s[3]=='144':
            k += 1
            s = 0
            for d in range(1,i+1):
              if i % d == 0 and d % 2 != 0:
                s += d
            print( i, s )
            if k == 7: break