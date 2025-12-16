# Автор: П. Финкель

s=open('24-278.txt').readline()
a='02468'
mx=0
for c in '13579QWERTYUIOPASDGHJZXCVBM':
    s=s.replace(c,' ')

for c in range(len(s)-1):
    if (s[c]in a) and (s[c+1]in a):s=s.replace(s[c]+s[c+1],s[c]+' '+s[c+1])
s=s.split()
for c in s:
    if c[0] in a and c[0]==c[-1] and len(c)>mx:mx=len(c)
print(mx-2)

