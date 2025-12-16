# Автор: К. Багдасарян

n = 0
for x in open('9-259.txt'):
    n += 1
    d = [int(z) for z in x.split()]
    if len(d) == len(set(d)):
        diffs = [d[i+1] - d[i] for i in range(5)]
        if len(set(diffs)) == 1:
            print(n)
            break


