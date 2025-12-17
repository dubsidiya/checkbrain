# Автор: Г. Шапошников

f=open("27-179a.txt")

n=int(f.readline())

startTime=[0]*n
endTime=[0]*n

for i in range(n):
    startTime[i],endTime[i]=map(int,f.readline().split())

busy=[0]

for i in range(1,n):
    b=True
    for j in range(len(busy)):
        for k in range(startTime[busy[j]],endTime[busy[j]]):
            if(k>=startTime[i] and k<=endTime[i]):
                b=False
                break
        if(b==False):
            break
    if(b):
        busy.append(i)

print(len(busy))
