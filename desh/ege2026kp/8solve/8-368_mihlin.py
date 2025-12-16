# Михлин Б.С.
'''
8.368 (Е. Джобс) Сколько существует чисел, пятнадцатеричная запись которых содержит
5 разрядов, причём разряды, кратные 2 и кратные 3, чередуются?
Например, число 40068 подходит под описание, число 40086 - нет.
'''
from itertools import *
# Способ 1:
r=[x for x in product(range(15),repeat=5) if x[0]!=0 and 
    (0==x[0]%2==x[1]%3==x[2]%2==x[3]%3==x[4]%2 or
     0==x[0]%3==x[1]%2==x[2]%3==x[3]%2==x[4]%3)]
print(len(r)) # Ответ: 17438
# Способ 2:
r=[(a,b,c,d,e) for a,b,c,d,e in product(range(15),repeat=5) if a!=0 and 
    (0==a%2==b%3==c%2==d%3==e%2 or 0==a%3==b%2==c%3==d%2==e%3)]                                         
print(len(r)) # Ответ: 17438
# Способ 3:
k=0
d2='02468ace' # цифры, кратные двум
d3='0369c'    # цифры, кратные трем
for a in '123456789abcde':
    for b in '0123456789abcde':
        for c in '0123456789abcde':
            for d in '0123456789abcde':
                for e in '0123456789abcde':
                    if a in d2 and b in d3 and c in d2 and d in d3 and e in d2 or\
                       a in d3 and b in d2 and c in d3 and d in d2 and e in d3:                     
                        k+=1
print(k) # Ответ: 17438
# Способ 4. Можно перебирать только цифры кратные 2 или 3:
k=0
d2='02468ace' # цифры, кратные двум
d3='0369c'    # цифры, кратные трем
for a in '234689ace':
    for b in '0234689ace':
        for c in '0234689ace':
            for d in '0234689ace':
                for e in '0234689ace':
                    if a in d2 and b in d3 and c in d2 and d in d3 and e in d2 or\
                       a in d3 and b in d2 and c in d3 and d in d2 and e in d3:                     
                        k+=1
print(k) # Ответ: 17438
