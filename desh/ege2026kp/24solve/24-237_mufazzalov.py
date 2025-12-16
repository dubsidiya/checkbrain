# Автор: Mufazzalov D.F.

s = open('24-237.txt').readline() + '.'

j = ans = 0
a = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        a += 1
    else:
        k = a // 3
        j += k
        ans = max(ans, j)
        if a % 3:
            j = k
        a = 1
print(ans * 3)