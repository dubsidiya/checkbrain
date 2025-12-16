# Автор: А. Агафонцев

k = 0

for i in range (1,10**7):
    if i%6 == 0 and i%8 == 0 and i%7 == 0:
        s = str(i)
        if s[1]+s[-1] == '66' and '6' in s[2:-2]:
           k += 1
           s = 0
           for d in range(1,i+1):
             if i % d == 0: s += d
           print(i, s)
           if k == 7:
               break