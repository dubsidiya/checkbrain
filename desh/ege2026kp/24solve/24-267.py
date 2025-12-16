# Автор: А. Кабанов

s = open('24-264.txt').readline()
for c in 'QWRTYUIOPSGHJKLZXVNM':
  s = s.replace( c, ' ' )

s = s.split()
print( max( s, key = len ) )
print( max( len(x) for x in s ) )
