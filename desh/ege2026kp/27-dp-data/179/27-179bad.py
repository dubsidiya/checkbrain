# Автор: Г. Шапошников
"""
Сохраняем список занятых промежутков времени. Для каждой поступившей заявки
проверяем находится ли хотя бы одна ее секунда хотя бы в одном из занятых
промежутков времени. Если да, то эту заявку не берем. В конце выводим
количество элементов в списке.
"""

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
