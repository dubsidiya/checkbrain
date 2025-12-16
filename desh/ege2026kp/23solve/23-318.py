def f( s, end, nCmd ):
  if nCmd == 0:
    return s[-1] == end and 'M' not in s
  return f( s+chr(ord(s[-1])+1), end, nCmd-1 ) + \
         f( s+chr(ord(s[-1])+4), end, nCmd-1 )

print( f( 'A', 'O', 5 ) )


# Автор: Д. Паршиков

"""
Представим, что каждая буква латинского алфавита - это цифра от 1 до 26
Исходная цепочка начинается с 1 и заканчивается в 15 и не содержит 13
"""
def f(a, c):
    if a == 13:
        return 0
    if c == 5:
        return a == 15
    return f(a + 1, c + 1) + f(a + 4, c + 1)

print(f(1, 0))
