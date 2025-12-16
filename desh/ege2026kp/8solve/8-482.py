from string import ascii_uppercase
from itertools import product

targetNo = 3282210

L = 1
while targetNo > 26**L:
  targetNo -= 26**L
  L += 1

for w in product( ascii_uppercase, repeat=L ):
  targetNo -= 1
  if targetNo == 0:
    print( ''.join(w) )
    break

# Автор: О. Лысенков

a = ''.join(list(sorted('QWERTYUIOPASDFGHJKLZXCVBNM')))
k = 3282210
x = 26
count = 1
#ищем длину слова
while k > x:
    k -= x
    x *= 26
    count += 1
s = ''
k -= 1   #вычитаем из номера слова среди всех слов длины count 1 чтобы нумерация начиналась с нуля
#переводим
while k != 0:
    s = a[k % 26] + s
    k //= 26
#дописываем нужное количество '0'(букв А)
s = 'A' * (count - len(s)) + s
print(s)