# Автор: О. Лысенков

#1 способ
f = open("17-440.txt")
a = [int(i) for i in f]
k = 0
sum_el_15 = 0
for i in range(len(a) - 2):
    if sum(a[i + j ] % 40 == 15 for j in range(3)) == 2:
        if sum(a[i + j] % 7 == 0 for j in range(3)) <= 2:
            k += 1
            if a[i] % 40 != 15:
                sum_el_15 += a[i]
            if a[i + 1] % 40 != 15:
                sum_el_15 += a[i + 1]
            if a[i + 2] % 40 != 15:
                sum_el_15 += a[i + 2]
print(k,sum_el_15)

#2 способ
f = open("17-440.txt")
a = [int(i) for i in f]
k = 0
sum_el_15 = 0
for i in range(len(a) - 2):
    if sum(a[i + j ] % 40 == 15 for j in range(3)) == 2:
        if sum(a[i + j] % 7 == 0 for j in range(3)) <= 2:
            k += 1
            sum_el_15 += sum(j for j in [a[i],a[i + 1],a[i + 2]] if j % 40 != 15)
print(k,sum_el_15)