# Коротков Михаил Сергеевич
# https://vk.com/mskorotkov

a = [[0, 0, 0] for _ in range(80)]

a[3] = [0, 1, 0]
for i in range(4, len(a)):
    a[i][0] += sum(a[i - 1]) - a[i - 1][0]
    a[i][1] += sum(a[i - 2])
    if i % 2 == 0:
        a[i][2] += sum(a[i // 2])
    if i == 11:
        a[:11] = [[0, 0, 0] for _ in range(11)]
    if i == 23:
        a[23] = [0, 0, 0]

print(sum(a[-1]))