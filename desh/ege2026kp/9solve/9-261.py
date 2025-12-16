# Автор: К. Багдасарян

count = 0
for x in open('9-259.txt'):
    d = [int(z) for z in x.split()]
    d3 = [z for z in d if abs(z) % 10 == 3]
    if len(d3) != 0:
        d.sort()
        diffs = [d[i+1] - d[i] for i in range(5)]
        if len(set(diffs)) == 1:
            count += 1
print(count)

