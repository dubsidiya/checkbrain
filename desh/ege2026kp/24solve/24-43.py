# Автор: В. Марченко

import re
n = 0
def newstr(matchobj): # matchobj - очередной найденный объект
    global n # переменная количества цепочек
    n += 1
    ss = matchobj.group() # найденная цепочка из объекта
    return str(len(ss))+'c'*len(ss)

s = open('k7-m5.txt').readline()

# Параметры re.sub : 1) Шаблон поиска.
#                    2) Функция поставляющая новую цепочку
#                    3) Исходная строка
s2 = re.sub(r'[C]+',newstr,s)
print(n)
print(s[:15], s[-15:])
print(s2[:15], s2[-15:])
