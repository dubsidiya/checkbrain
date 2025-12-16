# Автор: В. Марченко

import re

n = 0
def sd(matchobj):
    global n
    ss = matchobj.group()
    if ss[0] != 'J' and ss[-1] != 'J':
        n += 1
    return ss

s = open('24-J4.txt', "r").readline()
b = re.sub(r'J','JJJ',s) # Устраняем сцепление цепочек
c = re.sub(r'J?BOSSJ?',sd,b) # Ищем все цепочки с BOSS
print(n)

