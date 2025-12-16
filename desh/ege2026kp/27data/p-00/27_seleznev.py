f=open('27-p00b.txt')
data = [tuple(map(float, i.replace(',','.').split())) for i in f.readlines()]
a=[];b=[];c=[]
for x,y in data:
    if y>7: a.append((x,y))
    elif y<3: c.append((x,y))
    else: b.append((x,y))
mnRA=10**9
for i in range (len(a)-1):
    sa=0
    for j in range (1, len(a)):
        sa+=((a[j][0]-a[i][0])**2+(a[j][1]-a[i][1])**2)**0.5
    if sa<mnRA:
        mnRA=sa
        RA=i
mnRB=10**9
for i in range (len(b)-1):
    sb=0
    for j in range (1, len(b)):
        sb+=((b[j][0]-b[i][0])**2+(b[j][1]-b[i][1])**2)**0.5
    if sb<mnRB:
        mnRB=sb
        RB=i
mnRC=10**9
for i in range (len(c)-1):
    sc=0
    for j in range (1, len(c)):
        sc+=((c[j][0]-c[i][0])**2+(c[j][1]-c[i][1])**2)**0.5
    if sc<mnRC:
        mnRC=sc
        RC=i
Px=(a[RA][0]+b[RB][0]+c[RC][0])/3*10000
Py=(a[RA][1]+b[RB][1]+c[RC][1])/3*10000
print (Px,Py)
