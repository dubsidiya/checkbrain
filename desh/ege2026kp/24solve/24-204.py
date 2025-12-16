s0 = open('24-204.txt').readline().strip()

from re import findall

s = s0
chunk = r'(?:AA|CC)+'
pattern = fr'(?=({chunk}))'
parts = findall( pattern, s )
sMax = max( parts, key=len )
print( len(sMax)//2 )

# Автор: Е. Джобс

s = s0

mc = 0
for st in (0, 1):
    c = 0
    for i in range(st, len(s), 2):
        if s[i:i+2] in ('AA', 'CC'):
            c += 1
        else:
            c = 0
        mc = max(mc, c)
print( mc )
