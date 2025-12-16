# Автор: Е. Джобс

s = open('24-237.txt').readline()

mx_l = 0
for st in (0, 1, 2):
    # 012012012012012
    cur_l = 0
    for i in range(st, len(s), 3):
        ss = s[i:i+3]
        if len(ss) == 3:
            if ss[0]==ss[1]==ss[2]:
                cur_l += 3
            else:
                cur_l = 0
            mx_l = max(mx_l, cur_l)
print(mx_l)
