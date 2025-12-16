from re import findall

s = open('24-337.txt').readline()

num98 = r'[1-9A-D][0-9A-D]*(?:00|70)'
pattern = fr'(?=({num98}))'

parts = findall( pattern, s )
sMax = max( parts, key = len )
print( len(sMax), sMax)

# Автор: К. Багдасарян

s = open('24-337.txt').readline().strip()

n = len(s)
sub = sMax = ''
for i in range(n):
    if (s[i] in '123456789ABCD') or (s[i] == '0' and sub):
        sub += s[i]
        if i > 0 and s[i-1]+s[i] in ('70', '00'):
            if len(sub) > len(sMax):
                sMax = sub
    else:
        sub = ''
print( len(sMax), sMax )
