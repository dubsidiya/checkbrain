"""
Пример задания повышенной сложности:
**(А. Драганов). Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит
куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может:
а) убрать 4 камня или
б) убрать 7 камней или
в) уменьшить количество камней в куче в 2 раза (количество камней в куче, полученное
при делении, округляется до меньшего целого числа).
Выполнять ходы а) и б) можно только тогда, если в куче хватает камней для изъятия.
Игра завершается в тот момент, когда в куче останется менее 3 камней. Если при этом
в куче окажется чётное число камней, то победителем считается игрок, сделавший последний
ход. В противном случае победителем считается его противник. В начальный момент в куче
было S ≥ 3 камней.
Задание 19.
Укажите максимальное значение S, при котором у Пети есть выигрышная стратегия, причём
одновременно выполняются два условия:
− Петя не может гарантированно выиграть, сделав менее двух ходов;
− Петя может гарантированно выиграть, сделав не более двух ходов.
Задание 20.
Найдите два наименьших значения S, при которых у Вани есть выигрышная стратегия,
причём одновременно выполняются два условия:
− Ваня не может гарантированно выиграть, сделав менее двух ходов;
− Ваня может гарантированно выиграть, сделав не более двух ходов.
Найденные значения запишите в ответе в порядке возрастания.
Задание 21
У Пети была выигрышная стратегия, придерживаясь которой он мог гарантированно выиграть
при любых ходах Вани. Но Петя специально поддался. Петя сделал свой первый ход так,
что Ваня сделал только один ход, после которого игра сразу закончилась и Ваня победил.
Укажите наименьшее значение S, при котором такое возможно.
"""
def gameOver( x ):
  return x < 3

def moves( x ):
  if x >= 7:
    return x-4, x-7, x//2
  if x >= 4:
    return x-4, x//2
  return (x//2, )

def win0( x ): # выигрыш в результате хода соперника
  return gameOver(x) and x % 2 != 0

def lose0( x ): # проигрыш в результате хода соперника
  return gameOver(x) and x % 2 == 0

def lose10( x ): # проигрыш в 1 ход без хода соперника
  return not gameOver(x) and \
         all( win0(y) for y in moves(x) )

def win1( x ): # выигрыш, сделав не более 1 хода
  return not gameOver(x) and \
         any( lose0(y) or lose10(y) for y in moves(x) )

def lose1( x ): # проигрыш, сделав не более 1 хода
  return all( win1(y) or win0(y) for y in moves(x) )

def win2( x ):
  return not win1(x) and \
         any( lose1(y) for y in moves(x) )

def lose2( x ):
  return all( win1(y) or win2(y) for y in moves(x) ) and \
         any( win2(y) for y in moves(x) )

#print( 'w0:', [s for s in range(0,100) if win0(s)] )
#print( 'l0:', [s for s in range(0,100) if lose0(s)] )
#print( 'l10:', [s for s in range(0,100) if lose10(s)] )
#print( 'w1:', [s for s in range(3,100) if win1(s)] )
#print( 'l1:', [s for s in range(3,100) if lose1(s)] )
print( '19)', [s for s in range(3,100) if win2(s)] )
print( '20)', [s for s in range(3,100) if lose2(s)] )
print( '21)', [s for s in range(3,100)
                 if (win1(s) or win2(s)) and
                     any( win1(y) for y in moves(s) )])

# Автор: А. Драганов

from functools import *
def H(p):
    if p<=3: return p//2, #важно ставить запятую или брать в квадратные скобки, иначе это не список
    if p<7: return p-4, p//2
    return p-4, p-7, p//2

@lru_cache(None)
def f(p):
    if p<3:
        return 'L' if p%2==0 else 'P'
    return 'W' if any(f(h)=='L' for h in H(p)) else 'L'

@lru_cache(None)
def c(p):
    if p<3: return 0
    if f(p)=='L': return 1+max(c(h) for h in H(p))
    return 1+min(c(h) for h in H(p) if f(h)=='L')

S = range(3, 300)
print('19:',[s for s in S if f(s)=='W' and c(s) in [3,4]][-1])
print('20:',[s for s in S if f(s)=='L' and c(s) in [4,5]][:2] )
print('21:',[s for s in S if f(s)=='W' and any( c(h)==1 and f(h)=='W' for h in H(s))][0])

# Автор: А. Драганов

from functools import  *
def H(p):
    if p==3: return [p//2] # важно возвращать список
    if p<7: return p-4, p//2
    return p-4, p-7, p//2
@lru_cache(None)
def f(p):
    if p<3: return 'L0' if p%2==0 else 'W0'
    if any(f(h) in 'L0' for h in H(p)): return 'W1'
    if all(f(h) in 'W0' for h in H(p)): return 'L1'
    if any(f(h) in 'L0L1' for h in H(p)): return 'W2'
    if all(f(h) in 'W0W1' for h in H(p)): return 'L2'
    if any(f(h) in 'L0L1L2' for h in H(p)): return 'W3'
    if all(f(h) in 'W0W1W2' for h in H(p)): return 'L3'
    if any(f(h) in 'L0L1L2L3' for h in H(p)): return 'W4'
    if all(f(h) in 'W0W1W2W3' for h in H(p)): return 'L4'
    if any(f(h) in 'L0L1L2L3L5' for h in H(p)): return 'W5'
    if all(f(h) in 'W0W1W3W4W5' for h in H(p)): return 'L5'
    return '--'
S = range(3,300)
print('19:',[s for s in S if f(s) in 'W3W4'][-1] )
print('20:',[s for s in S if f(s) in 'L4L5'][:2])
print('21:',[s for s in S if f(s)[0]=='W' and any(f(h) in 'W1W2' for h in H(s))][0])

# Автор: А. Драганов

from functools import *
def H(p): return [h for h in [p-4,p-7,p//2] if h>=0 and h<p]
@lru_cache(None)
def f(p,n):
    if p<3:
        if p%2==0: return n%2==0
        else: return n%2==1
    if n ==-1: return 0
    W = [f(h, n-1) for h in H(p)]
    return all(W) if n%2==0 else any(W)
S = range(3,300)
print('19:', [s for s in S if f(s,3) and not f(s,1)][-1])
print('20:', [s for s in S if f(s,4) and not f(s,2)][:2])
def f0(p,n):
    if p<3:
        if p%2==0: return n%2==0
        else: return n%2==1
    if n == 0: return 0
    W = [f0(h, n-1) for h in H(p)]
    return all(W) if n%2==0 else any(W)
print('21:', [s for s in S if f(s,301) and any(f0(h,1) and h>=3 for h in H(s) ) ] [0])
