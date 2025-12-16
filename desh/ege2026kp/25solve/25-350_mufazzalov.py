from fnmatch import fnmatch
# Mufazzalov D.F.

def check(m):
    global prime
    for dev in prime:
        if dev * dev > m: return 1
        if m % dev == 0: return 0


def get_prime(n):
    global prime
    prime = [2, 3]
    [prime.append(j) for j in range(5, n + 1, 2) if check(j)]
    return prime


end = 10 ** 11
prime, a = get_prime(int(end ** 0.5)), []
for i in prime:
    for k in prime[1:]:
        if (num := i ** (k - 1)) >= end: break
        if num % 10 <= 1 or not fnmatch(str(num), '*2025*'): continue
        a.append((num, num // i))
a.sort(key=lambda x: x[1])
for ai in a:
  print( *ai )
