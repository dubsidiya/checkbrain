# Автор: Р. Косов

for p in range(7, 30):
   n1 = int('2465123', p)
   n2 = int('251341', p)
   s = n1 + n2
   #print(p, s)
   if s % 17 == 0:
       print(s // 17)
       break