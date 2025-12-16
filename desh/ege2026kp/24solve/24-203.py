# Автор: Н. Егорова

f=open('24-203.txt')
s=f.read()

b={'A':-1,'B':-1,'C':-1}
k=0
b[s[0]]=0
for i in range(1,len(s)):
    b[s[i]]=i
    m=min([b[j] for j in b if j!=s[i]])
    k+=i-m-2
print(k)
f.close()


