# Автор: К. Багдасарян

n = 0
m = -1
for x in open('9-259.txt'):
    n += 1
    d = [int(z) for z in x.split()]
    if d[0] == max(d) and d[-1] == min(d):
        if d[1]<d[2]<d[3]<d[4]:
            if (d[0] + d[-1])/2 in d:
                m = n
print(m)




