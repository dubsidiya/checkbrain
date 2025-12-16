# Автор В.Н. Шубинкин
from string import ascii_uppercase

def is_alternate(s):
    for i in range(len(s) - 1):
        if (s[i] in even_digits) == (s[i + 1] in even_digits):
            return False
    return True

with open('24-268.txt') as f:
    s = f.read().strip()
alphabet = '0123456789' + ascii_uppercase[:20]
even_digits = alphabet[::2]
to_remove = ascii_uppercase[20:]
for letter in to_remove:
    s = s.replace(letter, ' ')
numbers = list(filter(lambda num: num[0] != '0' and is_alternate(num), s.split()))
max_len = len(max(numbers, key=len))
numbers_with_max_len = list(filter(lambda num: len(num) == max_len, numbers))
print(min(numbers_with_max_len))
