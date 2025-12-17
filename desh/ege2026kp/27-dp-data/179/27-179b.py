# Автор: Г. Шапошников
"""
Сохраняем список занятых промежутков времени, но проверяем для поступившей
заявки не каждую секунду отдельно, а сравниваем промежутки времени на наличие
пересечения сразу. Если пересечения нет, то берем заявку.
"""

f=open("27-179b.txt")

n=int(f.readline())
busy=[]

for i in range(n):
    s,e=map(int,f.readline().split())

    haveSlot=True
    for el in busy:
        if (el[0]==s):
            haveSlot=False
            break
        elif (el[0]>s and e>el[0]):
            haveSlot=False
            break
        elif (s>el[0] and s<el[1]):
            haveSlot=False
            break


    if(haveSlot):
        busy.append([s,e])

print(len(busy))
