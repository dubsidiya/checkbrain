# Автор: М. Киртаев

st = open('24-298.txt').readline()
#st = '1*0+12*0+78888*8*9'
m = 0
for l in range(len(st)):
    for r in range(l+m, len(st)):
        ps = st[l:r+1]
        if ps[-1] in '-*': continue
        if (ps[0] in '*-0' or '--' in ps or '**' in ps or '-*' in ps
                or '*-' in ps or '-0' in ps or '*0' in ps):
            break
        else:
            m = max(m, len(ps))
#            print(ps, len(ps))
print(m)