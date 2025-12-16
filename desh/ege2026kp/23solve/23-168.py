# Автор: М. Фирсов

# 1-й способ
a = [1]#Начальное число
for _ in range(10): #Кол-во команд
    b = []
    for i in a:
        b.append(i + 4)
        b.append(i + 7)
        b.append(int(i / 2)) #Выбор int() вместо // связан с особенностью языка Python,
                             #при работе с отрицательными числами. В рамках данной задачи,
                             #выбор // на ответ не повлияет.
    a, b = b, []
print(a.count(1))

# 2-й способ
def f(x, cnt):
    if cnt == 10:
      return x == 1
    return f(x + 4, cnt + 1) + f(x + 7, cnt + 1) + f(x // 2, cnt + 1)
print(f(1, 0))






