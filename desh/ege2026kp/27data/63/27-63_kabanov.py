with open('27-63a.txt') as f:
    clustersA = [[] for i in range(3)]
    for s in f:
        x,y = [float(d) for d in s.replace(',','.').split()]
        if x>5 and y<5: clustersA[0].append([x,y])
        elif x>5 and y>5: clustersA[1].append([x,y])
        else: clustersA[2].append([x,y])

with open('27-63b.txt') as f:
    clustersB = [[] for i in range(5)]
    for s in f:
        x,y = [float(d) for d in s.replace(',','.').split()]
        if x>10 and y>x: clustersB[0].append([x,y])
        elif y<x and y>10: clustersB[1].append([x,y])
        elif y<10 and y>-x+20: clustersB[2].append([x,y])
        elif y<10 and y>x: clustersB[3].append([x,y])
        else: clustersB[4].append([x,y])

def dist(p1,p2):
    x1,y1,x2,y2 = *p1, *p2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p1) for p1 in kl)
        m.append([sm,p])
    return min(m)[1]

centersA = [center(k) for k in clustersA]
px = sum(x for x,y in centersA)/len(centersA)*100000
py = sum(y for x,y in centersA)/len(centersA)*100000
print(int(px), int(py))

centersB = [center(k) for k in clustersB]
px = sum(x for x,y in centersB)/len(centersB)*100000
py = sum(y for x,y in centersB)/len(centersB)*100000
print(int(px), int(py))


