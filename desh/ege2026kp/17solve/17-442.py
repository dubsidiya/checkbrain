# Автор: О. Лысенков

#1 способ
f = open('17-442.txt')
a = [int(i) for i in f]
count = 0
sum_el = 0
max_el_37 = max(i for i in a if i % 100 == 37)
for i in range(len(a) - 3):
    if (((a[i] > max_el_37) + (a[i + 1] > max_el_37) + (a[i + 2] > max_el_37)  + (a[i + 3] > max_el_37)) == 2 and
            ((a[i] % 10 == a[i] // 10 % 10) + (a[i + 1] % 10 == a[i + 1] // 10 % 10) +
             (a[i + 2] % 10 == a[i + 2] // 10 % 10) + (a[i + 3] % 10 == a[i + 3] // 10 % 10)) == 1): #если числа были
#бы не натуральные, а просто целые, то была бы проблема 0 % 10 = 0 // 10 % 10,
#но в случае с натуральными такой проблемы нет, так как, если число длины 1, то при делении его на 10
#получится 0, а последняя цифра не может быть равна 0 для натурального числа длины 1
        count += 1
        if a[i] % 10 == a[i] // 10 % 10:
            sum_el += a[i]
        elif a[i + 1] % 10 == a[i + 1] // 10 % 10:
            sum_el += a[i + 1]
        elif a[i + 2] % 10 == a[i + 2] // 10 % 10:
            sum_el += a[i + 2]
        else:
            sum_el += a[i + 3]
print(count,sum_el)

#2 способ
f = open('17-442.txt')
a = [int(i) for i in f]
count = 0
sum_el = 0
max_el_37 = max(i for i in a if i % 100 == 37)
for i in range(len(a) - 3):
    if (sum(a[i + j] > max_el_37 for j in range(4)) == 2 and
        sum(a[i + j] % 10 == a[i + j] // 10 % 10 for j in range(4)) == 1):
        count += 1
        sum_el += sum(a[i + j] for j in range(4) if a[i + j] % 10 == a[i + j] // 10 % 10)
print(count,sum_el)