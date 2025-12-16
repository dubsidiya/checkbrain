# Автор: А. Кабанов

s = open('24-300.txt').readline()

#---------------------------------------------------------
# Решение с помощью регулярных выражений
#---------------------------------------------------------
from re import finditer
number = r"([1-9]\d*|0)"
prod = fr"(({number}\*)*0(\*{number})*)"
pattern = fr"{prod}(\+{prod})+"
parts = [ x.group() for x in finditer( pattern, s ) ]
sMax = max( parts, key=len )

print( len(sMax), sMax )
print( eval(sMax) )

