r = 'XYZ'
m = n = k = 0
for s in open('24-169.txt').readline():
    if s != r[k % 3]:
        m = 0
        k = r.index(s)
    m += 1
    k += 1
    n = max(m, n)
print(n)