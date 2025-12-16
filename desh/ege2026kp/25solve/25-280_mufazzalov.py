# Mufazzalov
import fnmatch
pattern = '*2*0*2*3*'
for i in range(1, 2023 ** 2):
    b = bin(i)[2:]
    o = oct(i)[2:]
    if b == b[::-1] and o == o[::-1]:
        if fnmatch.fnmatch(str(i), pattern):
            print(i, sum(map(int, o)))
