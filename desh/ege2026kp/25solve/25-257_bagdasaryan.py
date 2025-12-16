# Автор: К. Багдасарян

even = '02468'
odd = '13579'
k = 206
for i in range(1231056, 12399857, k):
    s = str(i)
    if s[:3] == '123' and s[-4] in odd and s[-3] in even and s[-2:] == '56':
            print(i, i//k)

