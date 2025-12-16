# Автор: Д. Муфаззалов

with open('26-154.txt') as F:
    n, data = int(F.readline()), []
    for _ in range(n):
        id_st, *marks = map(int, F.readline().split())
        data.append((id_st, sum(marks), marks.count(2)))

data.sort(key=lambda x: (x[2], -x[1], x[0]))

print( data[n // 4 - 1][0],
       list(filter(lambda x: x[2] > 2, data))[0][0] )
