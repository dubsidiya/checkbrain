# Автор? А. Богданов

count = 0
for s in open('9-209.csv'):
   data = sorted( map(int, s.split(';')) )
   if len(set(data)) == 5:
     a, b, c, d, e = data
     if 2*c > e and 2*c > 3*a:
       print( s, end="" )
       count += 1
print( count )
