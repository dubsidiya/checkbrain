# Автор: В. Глезденев

from math import dist

def f_01( x, y ):    # функция распределения по кластерам
    if y>9.5-1/4*x: return 0
    if x<4.5 or y>4.5 and x<7.5: return 1
    else: return 2
k = 3  # количество кластеров
klas = [ [] for i in range(k) ]     #массив точек по кластерам
for s in open("27-92b.txt"):
    x, y = map(float, s.replace(',','.').split())
    klas[f_01(x,y)].append( (x, y) )
cent = []    # центроиды
for i in range(k): #обработка по кластерам
  mSd = float('inf')  #мин. сум. рас. больше 10**18
  for pC in klas[i]:   # цикл по точкам - центрам
    sumD = sum( dist(pC,p) for p in klas[i] ) # цикл по всем точкам
    if sumD < mSd:
      mSd = sumD; cen = pC
  cent.append( cen )

s0=[sum(x) for x in zip(*cent)]

print( int(s0[0]/k*100000), int(s0[1]/k*100000))

from turtle import *
tracer(0)
up()
hideturtle()
colors = ['red', 'green', 'blue', 'magenta', 'brown', 'cyan']
scale, shiftX, shiftY = 50, 300, 300
for i, cluster in enumerate(klas):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
