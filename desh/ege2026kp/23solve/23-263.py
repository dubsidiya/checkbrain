# Автор: Е. Джобс

def f(a, c):
    if c == 4:
        return {a}
    return f(a+2, c+1) | f(a*3, c+1)
print(len(f(1, 0)))
