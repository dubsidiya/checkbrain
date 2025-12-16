# Автор: Е. Джобс

for q in range(10):
    x  = int(f'123{q}45679')
    if x % 4013 == 0:
        print(x, x // 4013)

for q in range(10):
    for s in range(10):
        x  = int(f'123{q}4{s}5679')
        if x % 4013 == 0:
            print(x, x // 4013)

for q in range(10):
    for s in range(100):
        x  = int(f'123{q}4{s:02}5679')
        #x = 123*10**8 + q*10**7 + 4*10**6 + s*10**4 + 5679
        if x % 4013 == 0:
            print(x, x // 4013)

for q in range(10):
    for s in range(1000):
        x  = int(f'123{q}4{s:03}5679')
        if x % 4013 == 0:
            print(x, x // 4013)
