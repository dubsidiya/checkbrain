# Автор: М. Панькова

fin=open('9-210.csv')
otv=0

for y in fin:
  a = sorted(map(int,y.split(';')))
  b = set(a)
  S = 0
  for x in a:
    if a.count(x) > 1:
      S += x
  if a[-1] != a[-2] and len(b) < len(a) and a[0] + a[-1] > S:
    otv += 1

print(otv)