s = open('24-305.txt').read()

#---------------------------------------------------------
# Решение с помощью регулярных выражений
#---------------------------------------------------------
from re import finditer
number = r"([1-9]\d*|0)"
pattern = fr"AF{number}([\+\*]{number})*"
parts = [ x.group() for x in finditer( pattern, s ) ]
sMax = max( parts, key=len )

print( len(sMax), sMax )

