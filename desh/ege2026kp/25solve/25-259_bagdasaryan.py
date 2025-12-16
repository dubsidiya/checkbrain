# Автор: К. Багдасарян

even = '02468'
odd = '13579'
k = 2023
for i in range(11001074, 11899912, k):
    s = str(i)
    if s[2] in even and s[-3] in odd and s[-2:] == '11':
            print(i, i//k)



