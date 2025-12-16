# Автор: А. Орешкин

s=open('24-s2.txt').readline().strip()
ss='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
h=[0]*26
for x in ss:
    fr='X'+x+'Z'
    h[ss.find(x)]=s.count(fr)
k=h.index(max(h))
print(ss[k]+str(max(h)))

#X73
