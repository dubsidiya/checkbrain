# Автор: М. Бердышева 

#------------- Решение 1 --------------------
f=open('24-j7.txt')
s=f.read()
k=0
maxk=0
for i in range(len(s)-2):
    if int(s[i])%2==int(s[i+1])%2:
      k+=1
    else:
      maxk=max(maxk,k)
      k=0
print (maxk+1)


#------------- Решение 2 --------------------
def countj(s1):
    ss=s1
    kk=0
    while s.count(ss):
        ss=ss+s1
        kk+=1
    return kk
    
f=open('24-j7.txt')
s=f.read()
for i in range(2,10):
    s=s.replace(str(i),str(i%2))

print (max(countj('0'),countj('1')))
