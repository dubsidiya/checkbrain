# Автор: Е. Джобс

kr = 111
with open('27-171a.txt') as f:
    n, k = map(int, f.readline().split())
    s = [int(f.readline()) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i+k, n+1):
        if sum(s[i: j]) % kr == 0:
            cnt += 1
print(cnt)


#kr = 10
#n, k = 6, 3
#s = [4,6,2,6,3,1]
kr = 111
with open('27-171b.txt') as f:
    n, k = map(int, f.readline().split())
    s = [int(f.readline()) for _ in range(n)]

# количество сумм на k и более левее
#с остатком при делении на kr равным индексу
sk = [0]*kr
# 1 потому что пустая сумма равна 0 (без элементов)
sk[0] = 1
# сумма на k элементов левее
s_beg = 0
# сумма текущяя
s_k = sum(s[:k])
# найденное количество
cnt = 0
if s_k % kr == 0:
    cnt = 1
for i in range(k, n):
    s_beg += s[i-k]
    sk[s_beg % kr] += 1
    s_k += s[i]
    cnt += sk[s_k % kr]
print(cnt)







