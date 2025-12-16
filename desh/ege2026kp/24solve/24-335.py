s0 = open('24-335.txt').readline()

#--------------------------------------------

# Автор: И. Карпачев

from re import findall

s = s0

numEven = r'(?:(?:[1-9][0-9]*[02468])|(?:[2468]))'
numOdd = r'(?:(?:[1-9][0-9]*[13579])|(?:[13579]))'

pattern = rf'(?:(?:[/(]{numEven}[\+\-]{numOdd}[/)])+)'
pattern = rf'(?=({pattern}))'

res = findall( pattern, s )
m = max( res, key=len )
print( len(m), m )
