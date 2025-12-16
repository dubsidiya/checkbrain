# Автор: В. Марченко

import re
n = nc = 0
np = 1
def newstr(matchobj): # matchobj - очередной найденный объект
    global n  # переменная количество C-подцепочек
    global nc # переменная суммарной длины цепочек
    global np #  переменная произведения длин C-подцепочек
    n += 1
    ss = matchobj.group() # найденная цепочка из объекта
    nc += len(ss)
    np *= len(ss)
    return ''

s = open('k7-m7.txt').readline()

# Параметры re.sub : 1) Шаблон поиска.
#                    2) Функция поставляющая новую цепочку
#                    3) Исходная строка
s2 = re.sub(r'[C]+',newstr,s)
s3 = str(nc) + 'C'*nc + str(np) + s2
print(n)
print(s[:35])
print(s3[:35])
