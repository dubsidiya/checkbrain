# Автор: О. Лысенков

from re import  *
f = open(r"24-320.txt")
s = f.readline()
num = r'(([1-9]([0-9])+)|[0-9])'
mask = fr'(?=({num}(={num})+))'
ans = 0
for n in finditer(mask, s):
    z = n.group(1)
    m = z.split('=')
    if any(len(j) == 5 and sorted(j) == list(j) for j in m):
        ans = max(ans,len(z))
    else:
      for j in range(len(m)):
        if len(m[j]) >= 5:
            b = m[j][:5]
            if sorted(b) == list(b):
                ans = max(ans,len('='.join(m[:j])) + 6) #+5 символов наше b и ещё = не забыть!
print(ans)