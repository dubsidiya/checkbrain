# Автор: О. Лысенков

f = open("17-439.txt")
a = [int(i) for i in f]
k = 0
sum_el_17 = 0
for i in range(len(a) - 1):
    if ((a[i] % 80 == 17) + (a[i + 1] % 80 == 17)) == 1:
        if a[i] % 7 == 0 and a[i + 1] % 7 == 0:
            k += 1
            sum_el_17 += a[i] if a[i] % 80 == 17 else a[i + 1]
print(k,sum_el_17)