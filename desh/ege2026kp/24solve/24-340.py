from re import findall

s = open('24-337.txt').readline()

num8 = r'[1-9A-F][0-9A-F]*(?:0|8)'
pattern = fr'(?=({num8}))'

parts = findall( pattern, s )
sMax = max( parts, key = len )
print( len(sMax), sMax)

# Автор: К. Багдасарян

s = open('24-337.txt').readline()
sub = sMax = ''
for c in s:
    if (c in '123456789ABCDEF') or (c == '0' and sub):
        sub += c
        if c in '08':
            if len(sub) > len(sMax):
                sMax = sub
    else:
        sub = ''
print( len(sMax), sMax )


