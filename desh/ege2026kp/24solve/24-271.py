# Автор В.Н. Шубинкин

from string import ascii_uppercase, digits

def is_color(s):
    return all(map(lambda c: c in hex_digits, s))

hex_digits = digits + ascii_uppercase[:6]
with open('24-271.txt') as f:
    s = f.read().strip()

count = 0
for i in range(len(s) - 6):
    if s[i] == '#':
        ss = s[i+1:i+7]
        if is_color(ss):
            r, g, b = ss[:2], ss[2:4], ss[4:]
            count += g < r > b
print(count)
