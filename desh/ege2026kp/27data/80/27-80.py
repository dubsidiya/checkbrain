clustersA = [[] for i in range(4)]
for s in open('27-80a.txt'):
    x,y = [float(d) for d in s.replace(',','.').split()]
    if x<0 and y>0:
        clustersA[0].append([x,y])
    if x<2 and y<0:
        clustersA[1].append([x,y])
    if x>2 and y>2:
        clustersA[2].append([x,y])
    if x>3 and y<1.5:
        clustersA[3].append([x,y])
#print([len(cl) for cl in clustersA])

clustersB = [[] for i in range(7)]
for s in open('27-80b.txt'):
    x,y = [float(d) for d in s.replace(',','.').split()]
    if x>6 and y>3:
        clustersB[0].append([x,y])
    elif x>1 and y>1:
        clustersB[1].append([x,y])
    elif x>6:
        clustersB[2].append([x,y])
    elif x>1:
        clustersB[3].append([x,y])
    elif y<-4:
        clustersB[4].append([x,y])
    elif x<-4:
        clustersB[5].append([x,y])
    else:
        clustersB[6].append([x,y])
#print([len(cl) for cl in clustersB])

from math import dist

def Savg(cl):
    s = k = 0
    for p in cl:
        for p1 in cl:
            if p!=p1:
                s += dist(p,p1)
                k += 1
    return s/k

da = [Savg(cl) for cl in clustersA]
db = [Savg(cl) for cl in clustersB]

print(int(min(da)*100_000), int(max(da)*100_000))
print(int(min(db)*100_000), int(max(db)*100_000))





















