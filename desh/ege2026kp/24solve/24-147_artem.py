# Автор: А. Орешкин

s=open('24-s2.txt').readline().strip()
ss='BCDEFGHIJKLMNOPQRSTUVWXYZ'
h=[0]*25
for x in ss:
    fr='A'+x
    h[ss.find(x)]=s.count(fr)
k=h.index(max(h))
print(ss[k]+str(max(h)))
