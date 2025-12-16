# Автор: О. Лысенков

f = open("17-438.txt")
def one_is_equal_last(n):
    return str(abs(n))[0] == str(n)[-1]
a = [int(i) for i in f]
k = 0
sum_max_el = 0
for i in range(len(a) - 2):
    if (sum(one_is_equal_last(a[i + j]) for j in range(3)) == 1 and
        sum(len(str(abs(a[i + j]))) == 4 and str(abs(a[i + j]))[1] == '2'  for j in range(3)) == 2):
        k += 1
        sum_max_el += max(a[i],a[i + 1],a[i + 2])
print(k,sum_max_el)