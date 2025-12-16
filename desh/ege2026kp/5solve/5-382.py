"""
Автор: О. Лысенков

(О. Лысенков) На вход алгоритма подается целое неотрицательное число N. Алгоритм строит по нему новое число R по следующему правилу:
1) Число  N переводится в 30-ричную систему счисления.
2) Считается сумма значений цифр данного числа в 30-ричной системе счисления.
3) Сумма умножается на числовое значение последней десятичной цифры числа N.
Число R - это результат выполнения п. 3.

Найдите количество чисел N, меньших 1000, при которых
значение R кратно хотя бы одному простому числу, не равному R.

Примечание: 1 - не простое число.

Ответ: 970
"""
def toBase30( N ):
  N30 = []
  while N:
    N30 = [N%30] + N30
    N //= 30
  return N30

def alg( N ):
  N30 = toBase30( N )
  R = sum(N30) * (N % 10)
  return R

def valid( R ):
  if R < 2: return True
  if R == 2: return False
  for d in range(2,round(R**0.5)+1):
    if R % d == 0: return True
  return False

print( sum(1 for N in range(1000)
             if valid(alg(N)) ) )


# Автор: О. Лысенков

prostie=[int(j) for j in range(2,100000) if all(j%i!=0 for i in range(2,int(j**0.5)+1)) ]
def pr(n):
    if n < 2: return True
    for i in prostie:
        if  n%i==0 and i!=n:
            return i
    return False
def f(n):
    su=0
    x=n
    while n!=0:
        su+=n%30
        n//=30
    su*=(x%10)
    return su
k=0
for i in range(0,1000):
    if pr(f(i))!=0:
        k+=1

print(k)

# Автор: Д. Муфаззалов

def check(m):
    if m < 2: return 1
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0: return 1
    return 0

def f(n):
    s = 0
    while n:
        s += n % 30
        n //= 30
    return s

ans = sum([check(f(i) * (i % 10)) for i in range(1000)])

print(ans)


