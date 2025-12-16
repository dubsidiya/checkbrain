# Автор: А. Рогов

import csv

reader = csv.reader(open('9-170.csv'), delimiter=';')
k = 0
for line in reader:
    line = [int(i) for i in line]
    double = {i for i in line if line.count(i) == 2}
    single = [i for i in line if line.count(i) == 1]
    if len(single) == 4 and \
       sum(single) / len(single) <= double.pop() * 2:
        k += 1
print(k)
