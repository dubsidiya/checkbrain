# Автор: В. Глезденев

from math import dist
k = 3  #количество кластеров
klas = [ [] for i in range(k*2+1) ] #массив точек по кластерам (+1 аном.)
for s in open("27-94b.txt"):
    x, y = map(float,s.replace(',','.').split())
    d1=dist([x,y],[2.0,3.0])
    d2=dist([x,y],[10.0,3.0])
    d3=dist([x,y],[6.0,10.0])
    if d1>3.1 and d2>3.1 and d3>3.1: klas[6].append((x,y)) # continue
    if d1<3.1:
        klas[0].append((x,y))
        if d1<0.3: klas[1].append((x,y))
    elif d2<3.1:
        klas[2].append((x,y))
        if d2<0.3: klas[3].append((x,y))
    elif d3<3.1:
        klas[4].append((x,y))
        if d3<0.3: klas[5].append((x,y))
cent = []    # центроиды
for i in range(k):
  mSd = float('inf')  #мин. сум. рас. больше 10**18
  for pC in klas[i*2+1]:   # цикл по точкам - центрам
    sumD = sum( dist(pC,p) for p in klas[i*2] )
    if sumD < mSd:
      mSd = sumD; cen = pC
  cent.append( cen )
s0=[sum(x) for x in zip(*cent)]
print( int(s0[0]/k*100000), int(s0[1]/k*100000))

from turtle import *
tracer(0)
up()
hideturtle()
colors = ['red', 'green', 'blue', 'magenta', 'brown', 'cyan', 'black']
scale, shiftX, shiftY = 20, 200, 200
for i, cluster in enumerate(klas):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()

