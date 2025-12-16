# Автор: Е. Филина

count = 0
with open('9-170.csv') as fin:
    data = fin.readlines()
    print(data)
data2 = []
for i in data:
  data2.append([int(g) for g in i.split(';')])

for line in data2:
    m1 = set()
    m2 = set()
    for s in line:
        if s in m1:
            m2.add(s)
        else:
            m1.add(s)
    if len(m1) == 5:
        summa = sum(m1.difference(m2))
        if summa / 4 <= sum(m2) * 2:
            count += 1

print(count)