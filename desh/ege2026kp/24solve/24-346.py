# Автор: А. Кабанов

from re import findall

s0 = open('24-345.txt').readline()

s = s0

num14 = r'[1-9A-D][0-9A-D]*[02468AC]'
pattern = fr'(?=({num14}))'

parts = findall( pattern, s )
sMax = max( parts, key=lambda x: int(x,14)  )
print( s.find(sMax), len(sMax), sMax)

