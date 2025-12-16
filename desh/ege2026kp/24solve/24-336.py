s0 = open('24-335.txt').readline()

#--------------------------------------------

# Автор: И. Карпачев

from re import findall

s = s0

num4 = r'(?:[1-9][0-9]*[^05])'
num5 = r'(?:[1-9][0-9]*[05])'

pattern = rf'(?:(?:[/(]{num4}[\+\-]{num5}[/)])+)'
pattern = rf'(?=({pattern}))'

res = findall( pattern, s )
m = max( res, key=len )
print( len(m), m )
