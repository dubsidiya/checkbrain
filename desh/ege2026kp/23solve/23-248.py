from functools import cache

@cache
def F( start, end, prog = "" ):
  if start > end: return 0
  if start == end:
    return '1'*7 in prog and '2'*7 in prog and \
           '1'*8 not in prog and '2'*8 not in prog
  return F( start+2, end, prog+'1' ) + \
         F( start+sum(map(int, str(start))), end, prog+'2' )

print( F(1, 70) )


# Автор: Е. Фокин

from functools import *
from sys import*
setrecursionlimit(10000)
lru_cache(None)
cnt = 0
def r(a):
    return reduce(lambda x,y: x+y,[int(i) for i in a])
def f(x,y,tr):
    if x > y : return ' '
    if x == y: return tr + ' ' + str(y)+ 'div'
    if x < y: tr +=str(x) + ' '
    return f(x+r(str(x)),y,tr +f' +s ') + f(x+2,y,tr + ' +2 ')
for i in f(1,70,'').split('div'):
    numb = [n for n in i.split() if n.isdigit()]
    tr = [n for n in i.split() if n.isdigit() == False and n !=' ']
    l = ''.join(tr)
    if '+s'*7 in l and '+2'*7 in l and '+s'*8 not in l and '+2'* 8 not in l:
        cnt+=1
print(cnt)