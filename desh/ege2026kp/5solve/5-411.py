# Автор: В. Лашин

def tr(n):
    s = ''
    while n > 0:
        s = str(n%3)+s
        n //= 3
    return s
ans = []
for n in range(167, 10000):
    n3 = tr(n)
    sm3 = n3.count('1') + n3.count('2')*2
    if sm3 % 9 == 0:
        n3+='2'
    else:
        n3+=tr(sm3%9)
    R = int(n3, 3)
    ans.append(R)
print(min(ans))

