# Автор В.Н. Шубинкин
from string import ascii_uppercase

with open('24-268.txt') as f:
    s = f.read().strip()
to_remove = ascii_uppercase[9:]
for letter in to_remove:
    s = s.replace(letter, ' ')
numbers = sorted(s.split(), key=len, reverse=True)
for num in numbers:
    if num[0] != '0' and int(num, 19) % 2 == 0:
        print(num)
        break
