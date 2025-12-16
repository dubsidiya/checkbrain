# Автор: Е. Джобс

s = open('24-300.txt').readline()

#---------------------------------------------------------
# Решение с помощью регулярных выражений
#---------------------------------------------------------
from re import findall
number = r'(?:[1-9]\d*|0)'
product = fr'(?:(?:{number}\*)*0(?:\*{number})*)'
pattern = fr'{product}(?:\+{product})*'
parts = findall( pattern, s )
sMax = sorted( parts, key=len, reverse=True )[0]

print( len(sMax), sMax )
