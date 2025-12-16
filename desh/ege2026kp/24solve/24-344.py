from re import findall

s = open('24-337.txt').readline()

num7 = r'1[0-9A-D]*(?:0|7)'
pattern = fr'(?=({num7}))'

parts = findall( pattern, s )
sMax = max( parts, key = len )
print( len(sMax), sMax)

# Автор: К. Багдасарян

s = open('24-337.txt').readline()

sub = sMax = ''
for c in s:
    if (c in '023456789ABCD' and sub) or c == '1':
        sub += c
        if c in '07':
            if len(sub) > len(sMax):
                sMax = sub
    else:
        sub = ''
print( len(sMax), sMax )


