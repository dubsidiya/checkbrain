# Автор: Е. Джобс

def f(a, b):
    if a > b: return 0
    if a == b: return 1
    return f(a+1, b) + f(a+2, b) + f(a*3, b)

oba = f(6, 15)*f(15, 21)*f(21, 25)
c15 = f(6, 15)*f(15, 25) - oba
c21 = f(6, 21)*f(21, 25) - oba

print(c15 + c21)
