def f( start, end, L = 0):
    if start <= 0 or L > 7:
        return 0
    if start == end: return 1
    return f( start-5, end, L+1) + f( start+2, end, L+1 ) + \
           f( start**2, end, L+1 )

print( f(3, 28) )

# Автор: И. Карпачев

print("Список траекторий:")

def f(a, b, s=[]):
    s.append(a)
    if a <= 0 or len(s) > 8:
        return 0
    if a == b:
        print(s)
        return 1
    return f(a - 5, b, s[::]) + f(a + 2, b, s[::]) + f(a ** 2, b, s[::])

print(f(3, 28))

print("Последовательность команд:")
def f(a, b, s=''):
    if a <= 0 or len(s) > 7: return 0
    if a == b and len(s) == 7:
        print(s)
        return 1
    return f(a - 5, b, s + '1') + f(a + 2, b, s + '2') + f(a ** 2, b, s + '3')

print(f(3, 28))
