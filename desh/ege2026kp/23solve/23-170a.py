# Автор: А. Сапегин

def Evklid(a, b):
    if a == 0 or b == 0:
        return a + b
    elif a > b:
        return Evklid(a % b, b)
    else:
        return Evklid(a, b % a)

pairs = []

def Landysh(a, b, n = 0):
    global pairs
    if n == 3 and Evklid(a, b) == 1:
        pairs.append([a, b])
    if n < 3:
        Landysh(a + 3, b, n + 1)
        Landysh(a * 4, b, n + 1)
        Landysh(a, b + 5, n + 1)
        Landysh(a, b * 2, n + 1)

Landysh(2, 3)

answer = []
for i in pairs:
    if [i[0], i[1]] not in answer and [i[1], i[0]] not in answer:
        answer.append(i)
print(len(answer))
print(answer)