# Михлин Б.С.
'''
8.297 (М. Ишимов) Определите количество чисел, восьмеричная запись которых содержит ровно 5 цифр,
среди них две различные цифры, сумма которых является простым числом.
'''
def pr(n): # проверка числа n на простоту
    if n < 2:
        return 0
    if n == 2:
        return 1
    for d in range(2, n):
        if n % d == 0:
            return 0
    return 1

from itertools import *
r = [x for x in product('01234567', repeat=5) if x[0] != '0' and
     any(pr(int(d1) + int(d2)) for d1 in x for d2 in x if d1 != d2)]
print(len(r)) # Ответ: 27170
