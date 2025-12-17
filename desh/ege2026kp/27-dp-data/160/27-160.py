# Автор: Е. Джобс

with open('27-160b.txt') as f:
    n = int(f.readline())
    s = [int(f.readline()) for _ in range(n)]

c_s = sum(s)

s = s + s
ss = []
for i in range(n):
    j_sum = s[i]
    for j in range(i+1, i+n):
        if 2 <= j-i <= n-2:
            #j_sum = sum(s[i:j])
            if j_sum % (s[i] + s[j-1]) == 0:
                if (c_s - j_sum) % (s[i-1] + s[j]) == 0:
                    ss.append(s[i] + s[j-1] + s[i-1] + s[j])
        j_sum += s[j]
print(max(ss))


