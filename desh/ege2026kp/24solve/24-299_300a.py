# Автор: М. Киртаев

st = open('24-299.txt').readline()
#st = '1*0+12*0'
m = 0
for l in range(len(st)):
    for r in range(l+m, len(st)):
        ps = st[l:r+1]
        if (len(ps) > 1 and (ps[0] == '*' or ps[0] == '+' or '++' in ps
                             or '**' in ps or '+*' in ps or '*+' in ps
                             or '+00' in ps or '*00' in ps
                             or ps[:2] == '00')):
            break
        try:
            a = eval(ps)
        except:
            pass
        else:
            if a == 0:
                m = max(m, len(ps))
#                print(ps, len(ps))
print(m)