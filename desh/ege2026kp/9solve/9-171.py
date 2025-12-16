# Автор: А. Рогов

import csv

reader = csv.reader(open('9-170.csv'), delimiter=';')
k = 0
for line in reader:
    line = [int(i) for i in line]
    repeat = {i for i in line if line.count(i) == 3}
    single = [i for i in line if line.count(i) == 1]
    if len(single) == 3 and \
       3 * (single[0] + single[1] + single[2]) <= (w := repeat.pop()) ** 3:
        k += 1

print(k)
