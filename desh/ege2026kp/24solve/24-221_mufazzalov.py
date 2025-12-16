# Автор: Mufazzalov D.F.

s, ans = open('24-221.txt').readline(), 0

j = p = int(s[0] == '0')
for i in range(1, len(s)):
    if s[i] not in '01': j = p = 0
    if s[i] == '0':
        p = 1
        if s[i - 1] != '0':
            j = 0
    j += p
    if s[i] == '1': ans = max(ans, j)
print(ans)
