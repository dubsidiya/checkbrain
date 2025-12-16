# Автор: А. Кабанов

from re import findall

s0 = open('24-347.txt').readline()

s = s0

num15 = r'[1-9A-E][0-9A-E]*[05A]'
pattern = fr'(?=({num15}))'
parts = findall( pattern, s )
sMax = max( parts, key=lambda x: int(x,15)  )
print( s.find(sMax)+len(sMax)-1, len(sMax), sMax)

