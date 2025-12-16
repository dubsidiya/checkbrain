# Автор: А. Гнедов

s = open('24-208.txt').readline()
# s = '1' * 500 + '2022022333' * 8 + '4' * 1000

ans = 0
pos = 0  # первая позиция, входящая в последовательность
sub = '2022'
buf = [0] * 5
while True:
    pos = s.find(sub, buf[-1])
    if pos == -1:
        ans = max(ans, len(s) - buf[0])
        break
    else:
        ans = max(ans, pos - buf.pop(0) + 3)
        buf.append(pos + 1)
print(ans)
