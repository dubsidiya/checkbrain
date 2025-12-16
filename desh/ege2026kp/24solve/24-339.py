from re import findall

s = open('24-337.txt').readline()

num5 = r'[1-9]\d*(?:0|5)'
pattern = fr'(?=({num5}))'

parts = findall( pattern, s )
sMax = max( parts, key = len )
print( len(sMax), sMax)

# Автор: К. Багдасарян

s = open('24-337.txt').readline()
sub = sMax = ''
for c in s:
    if (c in '123456789') or (c == '0' and sub):
        sub += c
        if c in '05':
            if len(sub) > len(sMax):
                sMax = sub
    else:
        sub = ''
print( len(sMax), sMax )


