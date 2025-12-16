# Автор: К. Багдасарян

even = '02468'
odd = '13579'
k = 92
for i in range(12041696, 12849699, k):
    s = str(i)
    if s[3] == '4' and s[2] in even and s[4] in odd and s[-3]=='6' and s[-1] == '8':
        print(i, i//k)


