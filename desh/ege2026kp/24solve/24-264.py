# Автор: Е. Джобс

s = open('24-264.txt').readline()
digits = set('0123456789')
letters = set(s) - digits

for c in letters:
    s = s.replace(c, 'A')

# заменяем все буква+цифра на буква+пробел+цифра
# и цифра+буква на цифра+пробел+буква
for d in digits:
    s = s.replace('A'+d, 'A '+d).replace(d+'A', d+' A')

words = [x if x[0] == 'A' or x[0] != '0' and x[-1] not in '13579' else ' '
         for x in s.split()]
s = ''.join(words)
while 'A ' in s or ' A' in s:
    s = s.replace('A ', ' ').replace(' A', ' ')
print(max(map(len, s.split())))
