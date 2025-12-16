# Автор: А. Богданов

s = open('24-275.txt').read()
k = m = 0
for i in range(len(s)-1):
  if s[i]+s[i+1] not in 'XYZX':
    k += 1
    if m<k:
      j = i
      m = k
  else:
    k = 0
print(m-1)