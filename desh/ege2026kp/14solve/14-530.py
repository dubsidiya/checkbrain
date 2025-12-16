# Автор: Р. Косов

for p in range(18, 30):
   n1 = int('22A12E', p)
   n2 = int('2F1391', p)
   n3 = int('1H05D0',p)
   s = n1 + n2 - n3
   #print(p, s)
   if s % 19 == 0:
       print(s // 19)
       break
