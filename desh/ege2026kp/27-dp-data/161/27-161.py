# Автор: Е. Джобс

with open('27-161b.txt') as f:
    n, v = map(int, f.readline().split())
    s = [(int(f.readline()) + v - 1) // v for _ in range(n)]

#n, v = 6, 10
#s = [1, 5, 3, 7, 6, 4]
s = s*3
p = []
# st - стоимсоть доставки одной из машин
st1 = st2 = 0
# lt - ближайший к лаборатории пункт, из которого не забирали материалы,
# для машины слева
lt = n-1
# rt - ближайший к лаборатории пункт, из которого не забирали материалы,
# для машины справа
rt = n+1
for _ in range(n-1):
    # если стоимость справа больше, то берем еще один пункт слева
    if st1 < st2:
        st1 += (n-lt)*s[lt]
        lt -= 1
    # увеличиваем стоимость справа
    else:
        st2 += (rt-n)*s[rt]
        rt += 1
if st1 == st2:
    p.append(0)

from itertools import accumulate
pr = [0] + list(accumulate(s))
# 0 1 3 6 10 11 13 16 20 21 23 26 30
#   1 2 3 4  1  2  3  4  1  2  3  4
#       6 4
#       3+4+ 1
#            1+4
#            1+2
for i in range(n+1, 2*n):
  # увеличиваю стоимость доставки из каждого пункта слева на значение s[j]
  st1 += pr[i] - pr[lt+1]
  # уменьшаю стоимость доставки из каждого пункта справа на значение s[j]
  st2 -= pr[rt] - pr[i]
  while st2 < st1:
    lt += 1
    st1 -= (i-lt)*s[lt]
    st2 += (rt - i)*s[rt]
    rt += 1
  if st1 == st2:
    p.append( i % n )

print( p )
print(max(p))
