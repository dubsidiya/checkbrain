# Автор: andaran

# Наибольший общий делитель
from math import gcd

f = [int(x) for x in open("27-138b.txt")]
nums = f[1:]

# Ищем все делители 3888
divs = [d for d in range(1, 3888 + 1) if 3888 % d == 0]
pairs = [{x: 0 for x in divs} for _ in range(6)]

count = 0
# Второе число на 18 позиций дальше первого
for n1, n2 in zip(nums, nums[18:]):
    r_n1 = n1 % 6
    r_n2 = n2 % 6

    d = gcd(n1, 3888)
    pairs[(6 - r_n1) % 6][d] += 1

    for d in divs:
        if d*n2 % 3888 == 0:
            count += pairs[(6 - r_n2) % 6][d]

print(count)  # 1214 18712791