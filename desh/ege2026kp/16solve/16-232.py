from timeit import default_timer

t0 = default_timer()
F = [0, 2, 3, 0]
n = 3
count = 2
while True:
  F[n] = F[n-3] + n - 15
  if F[n] > 10**5: break
  count += 1
  n += 3
  F.extend( [0, 0, 0] )
print( count, default_timer()-t0 )

# Автор: О. Лысенков

from functools import  cache
@cache
def f(n):
    if n < 3:
        return n + 1
    elif n >= 3 and  n % 3 == 0:
        return f(n-3) + n - 15
    elif n >= 3 and n % 3 != 0:
        return  10 ** 10 #если к некратному 3-м прибавить 3, то оно будет не кратным 3, поэтому,
        # если выполняется условие n >= 3 and n % 3 != 0,
        # то функция будет бесконечно вызывать саму себя, чтобы в таких ситуациях не  получить
        # бесконечную рекурсию, будем возвращать сразу  10 в 10 степени, это число больше 10 в 5 степени,
        # так что такое изменение функции не повлияет на ответ в нашей задаче,
        # но в то же самое время  теперь у нас нет бесконечной рекурсии при попадании в этот elif
t0 = default_timer()
k = 0
for i in range(1,10000000):
    if f(i) <= 10 ** 5:
        k += 1
print(k, default_timer()-t0)