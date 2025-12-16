# Автор: Е. Джобс

s = open('24-222.txt').readline().strip()
w = s.split('A')[1:-1]
mx = 0
for a, b, c in zip(w, w[1:], w[2:]):
    if a == b == c:
        #                 A  *  A  *  A  *  A
        mx = max(mx, len('A'+a+'A'+b+'A'+c+'A'))
print(mx)
