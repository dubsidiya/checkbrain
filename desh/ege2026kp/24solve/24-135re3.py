# Автор: В. Марченко

import re
n = 0
s = open('24-J4.txt', "r").readline()
b = re.sub(r'J','JJ',s) # Устраняем сцепление цепочек (замена J на JJ)
for matchobj in re.finditer (r'J?BOSSJ?',b): # Ищем все цепочки с BOSS
    ss = matchobj.group()
    if ss[0] != 'J' and ss[-1] != 'J':
        n += 1
print(n)
