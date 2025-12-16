# Автор: Е. Джобс

from re import *

s = open('24-320.txt').readline() + '='

num = r'(?:0|[1-9]\d*)'
double = fr'({num})=\1(?==)'
exp = fr'(?:{num}=)*{double}(?:={num})*'
L1 = max( (len(m[0]) for m in finditer(exp, s)), default=0 )
#print( L1 )

num = r'(?:0|[1-9]\d*)'
double = fr'({num})=\1'
exp = fr'(?:{num}=)*{double}'
L2 = max( (len(m[0]) for m in finditer(exp, s)), default=0 )
#print( L2 )

print( max(L1, L2) )
