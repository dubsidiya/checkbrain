# Автор: Д. Муфаззалов

with open('26-105.txt') as f:
    n, s = map(int, f.readline().split())
    data = sorted([int(f.readline()) for i in range(n)])
    k, sum_full_price, sum_discount, count, ans2 = 6, 0, 0, 0, s

for j in range(n):
    i = j + 1
    m = j - i // k
    if i % k:
        sum_discount -= data[m]
        sum_full_price += data[m]
    sum_discount += data[j]
    if (balance := s - sum_full_price - sum_discount // 2) < 0: break
    ans2, count = balance, i
print(count, ans2)