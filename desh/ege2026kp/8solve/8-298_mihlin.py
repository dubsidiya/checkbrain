# Михлин Б.С.
'''
8.298 (М. Ишимов) Определите количество чисел, пятеричная запись которых содержит ровно 5 цифр,
причём каждая цифра отличается от соседних не менее, чем на 2.
'''
# Способ 1
from itertools import *
r = [x for x in product('01234', repeat=5) if x[0] != '0' and
     all(abs(int(x[i - 1]) - int(x[i])) >= 2 and abs(int(x[i]) - int(x[i + 1])) >= 2 for i in range(1, 4, 2))]
print(len(r)) # Ответ: 140

# Способ 2
k = 0
for a in '1234':
    for b in '01234':
        for c in '01234':
            for d in '01234':
                for e in '01234':
                    x = a + b + c + d + e
                    if abs(int(a) - int(b)) >= 2 and abs(int(b) - int(c)) >= 2 and \
                       abs(int(c) - int(d)) >= 2 and abs(int(d) - int(e)) >= 2:
                        k += 1
print(k) # Ответ: 140
