# Автор: А. Кабанов

a = []
for i in '0123456789':
    s = int(f'12{i}45')
    if s%51==0:
        a+=[(s,s//51)]

for i in '0123456789':
    s = int(f'1245{i}')
    if s%51==0:
        a+=[(s,s//51)]

for i in '0123456789':
    for j in '0123456789':
        s = int(f'12{i}{j}45')
        if s%51==0:
            a+=[(s,s//51)]

for i in '0123456789':
    for j in '0123456789':
        s = int(f'12{i}45{j}')
        if s%51==0:
            a+=[(s,s//51)]

for i in '0123456789':
    for j in '0123456789':
        s = int(f'1245{i}{j}')
        if s%51==0:
            a+=[(s,s//51)]
a.sort()
for x,y in a:
    print(x,y)
