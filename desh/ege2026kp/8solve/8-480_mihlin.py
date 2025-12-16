# Михлин Б.С.
'''
8.480 (О. Лысенков) Петя составляет список всех возможных кодов, составленных из заглавных латинских букв.
Сначала он выписывает в алфавитном порядке все коды, состоящие из одного символа (A, B, …, Z),
затем – тоже в алфавитном порядке – коды из двух символов (AA, AB, …, AZ, BA, BB, … ZZ),
далее идут трёхсимвольные коды (AAA, AAB, …, ZZZ) и так далее.
Какое слово в этом списке стоит под номером 777332? Нумерация начинается с единицы.
'''
'''
1.  A
2.  B
....
26. Z
27. AA
28. AB
.....
777332. -> слово?
Кстати, такой же порядок букв используется и для нумерации колонок в электронных таблицах (от A до XFD).
'''
# Способы получения латинского алфавита:
#   1. Набор всех латинских букв на клавиатуре, затем сортировка:
#al=''.join(sorted('QWERTYUIOPASDFGHJKLZXCVBNM'))
#   2. Использование модуля строковых констант:
#from string import *
#al=ascii_uppercase
#   3. Использование функций chr и ord:
#al=''
#for i in range(26):
    #al+=chr(ord('A')+i) # 'A' - латинская
#           Решение задачи:
# Способ 1. Использование 26-ой системы
al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 777332
d = []
while n:
    d = [n % 26] + d
    n //= 26
for c in d:
    print(al[c - 1], end='') # Ответ: AREWJ
print()
# print(d) # [1, 18, 5, 23, 10] -> AREWJ
# print(list(zip(range(1,27),'ABCDEFGHIJKLMNOPQRSTUVWXYZ',)))

# Способ 2. Функция product
from itertools import *
from sys import exit
n = 0
for k in range(1, 6):
    for x in product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=k):
        n += 1
        if n == 777332:
            print(''.join(x)) # Ответ: AREWJ
            # exit()

# Способ 3. Вложенные циклы
n = 0
al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for a in al:
    n += 1
for a in al:
    for b in al:
        n += 1
for a in al:
    for b in al:
        for c in al:
            n += 1
for a in al:
    for b in al:
        for c in al:
            for d in al:
                n += 1
for a in al:
    for b in al:
        for c in al:
            for d in al:
                for e in al:
                    n += 1
                    if n == 777332:
                        print(a + b + c + d + e)  # Ответ: AREWJ
                        exit()
