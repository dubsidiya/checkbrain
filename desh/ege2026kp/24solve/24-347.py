# Автор: А. Кабанов

from re import findall

s0 = open('24-347.txt').readline()

s = s0

num12 = r'[1-9AB][0-9AB]*[0369]'
pattern = fr'(?=({num12}))'
parts = findall( pattern, s )
sMax = max( parts, key=lambda x: int(x,12)  )
print( s.find(sMax), len(sMax), sMax)

