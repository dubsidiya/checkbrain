# Автор: А. Мурашева

f=open("24-200.txt").readlines()
k=0
a=set()
for i in range(len(f)):
    #print(f[i])
    y=f[i].split(".")
    #print(y)
    if int(y[0])==195 and 20<=int(y[1])<=29 and int(y[2])//100==1 and int(y[2])%10==5 and len(y[2])==3 and int(y[3])==14:
        a.add(f[i])
print(len(a))
