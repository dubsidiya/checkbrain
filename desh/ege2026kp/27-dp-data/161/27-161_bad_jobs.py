# Автор: Е. Джобс

with open('27-161a.txt') as f:
    n, v = map(int, f.readline().split())
    s = [(int(f.readline()) + v - 1) // v for _ in range(n)]

#n, v = 6, 10
#s = [1, 5, 3, 7, 6, 4]
s = s*3
p = []
for i in range(n, 2*n):
    # c1 - пункт для первой машины
    # c2 - пункт для второй машины
    for c1 in range(i - (n-2), i):
        c2 = c1 + n - 1
        # st1- стоимость перевозки первой машины от c1 до i
        st1 = 0
        for j in range(c1, i):
            st1 += abs(i - j)*s[j]
        # st1- стоимость перевозки второй машины от с2 до i
        st2 = 0
        for j in range(i+1, c2 + 1):
            st2 += abs(i - j)*s[j]

        if st1 == st2:
            p.append(i % n)
            break
print( p )
print(max(p))
