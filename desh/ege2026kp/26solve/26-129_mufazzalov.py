# Автор: Д. Муфаззалов

with open('26-129.txt') as f:
    data, count_previus, reviewed = [], 0, set()
    for i in range(int(f.readline())):
        sanding, painting = map(int, f.readline().split())
        data.append((sanding, 1, i))
        data.append((painting, 0, i))

data.sort()

for time, process, num in data:
    if num in reviewed: continue
    count_previus += process
    last = num
    reviewed.add(num)

print(last + 1, count_previus - (count_previus > 0))