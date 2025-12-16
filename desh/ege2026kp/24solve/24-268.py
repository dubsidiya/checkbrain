# Автор В.Н. Шубинкин
from string import ascii_uppercase

with open('24-268.txt') as f:
    s = f.read().strip()
digits_20 = '0123456789ABCDEFGHIJ'
even_digits = digits_20[::2]
to_remove = ascii_uppercase[10:]
for letter in to_remove:
    s = s.replace(letter, ' ')
numbers = sorted(s.split(), key=len, reverse=True)
for num in numbers:
    if num[0] != '0' and num[-1] in even_digits:
        print(num)
        break
