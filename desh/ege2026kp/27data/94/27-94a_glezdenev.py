# Автор: В. Глезденев

from math import dist

def f_01( x, y ):    # функция распределения по кластерам (+1 аном.)
    d1=dist([x,y],[2.0,3.0])
    d2=dist([x,y],[10.0,3.0])
    if d1<3.1: return 0
    elif d2<3.1: return 1
    else: return 2
k = 2  # количество кластеров
klas = [ [] for i in range(k+1) ] #массив точек по кластерам (+1 аном.)
for s in open("27-94a.txt"):
    x, y = map(float,s.replace(',','.').split())
    klas[f_01(x,y)].append( (x, y) )
cent = []    # центроиды
for i in range(k):
  mSd = float('inf')  #мин. сум. рас. больше 10**18
  for pC in klas[i]:   # цикл по точкам - центрам
    sumD = sum( dist(pC,p) for p in klas[i] )
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
scale, shiftX, shiftY = 30, 200, 200
for i, cluster in enumerate(klas):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()

