s0 = open('24-333.txt').readline()

from re import findall

s = s0
word = "[A-Za-z0-9]+"
pattern = fr"{word}(?:\.{word})*@(?:yandex.ru|gmail.com)"
parts = findall( pattern, s )
sMax = max( parts, key = len )

print( len(sMax), sMax )

print( '-----------------------------' )

# Автор: И. Карпачев

s = s0

m = ''
for server in ['@yandex.ru', '@gmail.com']:
    sub = ''
    for x in s:
        sub += x
        if '.@' in sub or '@.' in sub or '@@' in sub or '..' in sub:
            sub = ''
        if sub.endswith(server):
            name = sub.strip(server)
            k = name.rfind('@')
            name = name[k + 1:]
            m = max(m, name + server, key=len)
print(m)
print(len(m))



