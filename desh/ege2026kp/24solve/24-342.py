from re import findall

s = open('24-337.txt').readline()

num144 = r'[1-9AB][0-9AB]*00'
pattern = fr'(?=({num144}))'

parts = findall( pattern, s )
sMax = max( parts, key = len )
print( len(sMax), sMax)

# Автор: К. Багдасарян

s = open('24-337.txt').readline()
n = len(s)
sub = sMax = ''
for i in range(n):
    if (s[i] in '123456789AB') or (s[i] == '0' and sub):
        sub += s[i]
        if i > 0 and s[i-1]+s[i] == '00':
            if len(sub) > len(sMax):
                sMax = sub
    else:
        sub = ''
print( len(sMax), sMax )


