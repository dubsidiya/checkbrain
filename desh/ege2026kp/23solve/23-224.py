def isPrime( n ):
  return n > 1 and \
         all( n % d != 0 for d in range(2,round(n**0.5)+1) )

def valid( prog ):
   return sum( 1 for x in prog if isPrime(x) ) == 3

def f( start, end, prog = None ):
  if prog is None: prog = []
  return 0 if start > end or (start == end and not valid(prog)) else \
         1 if start == end else \
         f( start+2, end, prog+[start+2] ) + \
           f( start+3, end, prog+[start+3] )

print( f( 15, 34 ) )

# Автор: И. Кропачев

trajectory = list()

def is_simple(x):
    if x == 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def f(a, b, way=[]):
    way.append(a)
    if a > b:
        return 0
    if a == b:
        trajectory.append(way)
        way = []
        return 1
    return f(a + 2, b, way[::]) + f(a + 3, b, way[::])

print("Всего траекторий:", f(15, 34))
num = 0
print("Список траекторий содержащих ровно 3 простых числа:")
for  e in trajectory:
    k = 0
    for x in e:
        if is_simple(x):
            k = k + 1
    if k == 3:
        num += 1
        print(num, '|', *e)

