# Автор: Е. Джобс

with open('27-159b.txt') as f:
    n, k = map(int, f.readline().split())
    p = [int(f.readline()) for _ in range(n)]

mx = max(p[:k])
mx_k = -1
c_z = []
for i in range(k, n):
    mx_k = max(mx_k, p[i-k])
    if p[i] > mx:
        c_z.append(p[i] + mx_k)
        mx = p[i]

print(max(c_z))
