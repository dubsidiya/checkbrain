# Автор: А. Кабанов

for i in '0123456789':
    s = int(f'12{i}45')
    if s%169==0:
        print(s,s//169)

for i in '0123456789':
    for j in '0123456789':
        s = int(f'123{i}567{j}')
        if s%169==0:
            print(s,s//169)

for i in '0123456789':
    for j in '0123456789':
        for k in '0123456789':
            s = int(f'123{i}{j}567{k}')
            if s%169==0:
                print(s,s//169)
