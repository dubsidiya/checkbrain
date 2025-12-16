# Автор: К. Багдасарян

even = '02468'
odd = '13579'
k = 4023
for i in range(1013796, 1898990, k):
    s = str(i)
    if s[1] in even and s[3] in even and s[5] in even and s[2] in odd and s[4] in odd and s[6] in odd:
            print(i, i//k)





