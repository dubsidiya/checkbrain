# Автор: О. Лысенков

f = open("17-441.txt")
a = [int(i) for i in f]
k = 0
sum_el_93 = 0
max_el_93 = max(i for i in a if i % 100 == 93)
for i in range(len(a) - 1):
    if ((a[i] > max_el_93) + (a[i + 1] > max_el_93)) == 1:
        if str(a[i])[0] == '9' or str(a[i + 1])[0] == '9':
            k += 1
            sum_el_93 += a[i] if a[i] > max_el_93 else a[i + 1]
print(k,sum_el_93)