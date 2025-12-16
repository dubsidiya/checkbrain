# Автор: М. Шагитов

s = open('24-262.txt').readline()
m, target, CHECK = 0, 'SOLO', ''

def check(x):
    return sum(i.isdigit() for i in set(x)) >= 5

start_positions = [0]
for _ in range(6):
    start_positions.append(s.find(target, start_positions[-1] + 1))

while start_positions[-1] != -1:
    sub1, sub2 = s[start_positions[0]:start_positions[4] + 3], s[start_positions[0] + 1:start_positions[5] + 3]
    for sub in [sub1, sub2]:
        if check(sub):
            m = max(len(sub), m)
            CHECK = max(CHECK, sub, key=len)
    start_positions = start_positions[1:] + [s.find(target, start_positions[-1] + 1)]

print(m)
print(CHECK)
