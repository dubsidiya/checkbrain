# Автор: А. Кабанов

f = open('26-164.txt' )
N, K, M = [int(x) for x in f.readline().split()]
a = []
for _ in range(N):
  d, p = [int(x) for x in f.readline().split()]
  a.append([d,p])

a.sort(reverse=1)

l = [[10**20]*N for i in range (200)]
l[1] = [p for d, p in a]
for k in range (2, 200):
  for i in range (N):
    m = [ l[k-1][j] for j in range(i) \
          if a[j][0]-a[i][0]>=K and l[k-1][j]+a[i][1] <=M ]
    if m:
      l[k][i] = min(m)+a[i][1]
  print(k, min(l[k]))
  if min (l[k]) == 10**20:
    mk = k-1
    ms = min(l[mk])
    print (mk, ms, max(a[i] for i in range(N) if l[mk][i]==ms))
    break