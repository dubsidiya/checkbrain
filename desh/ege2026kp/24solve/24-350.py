# Автор: А. Кабанов

from re import findall

s0 = open('24-347.txt').readline()

s = s0

num8 = r'[1-7][0-7]*[0246]'
pattern = fr'(?=({num8}))'
parts = findall( pattern, s )
sMax = max( parts, key=lambda x: (len(x), -int(x,8))  )
print( s.find(sMax), len(sMax), sMax)

