# Автор: Р. Косов

for p in reversed(range(8, 30)):
   n1 = int('11353712', p)
   n2 = int('135421', p)
   s = n1 + n2
   #print(p, s)
   if s <= 10**9:
       print(s)
       break
