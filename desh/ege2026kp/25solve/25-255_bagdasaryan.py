# Автор: К. Багдасарян

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


k = 9797
for i in range(k, 3999992, k):
    s = str(i)
    if s[0] == '3' and s[-1] == '1' and isprime(int(s[1:-1])):
        print(i, i//k)

