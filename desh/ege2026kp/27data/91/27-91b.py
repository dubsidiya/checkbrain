# Автор: В. Глезденев

from math import dist

def f_01( x, y ):    # функция распределения по кластерам (+1 аном.)
    d1=dist([x,y],[3,4.5]); d2=dist([x,y],[11.5,4.5]); d3=dist([x,y],[7.5,-3])
    if d1<4: return 0
    elif d2<4: return 1
    elif d3<4: return 2
    else: return 3
k = 3  # количество кластеров
klas = [ [] for i in range(k+1) ]     #массив точек по кластерам (+1 аном.)
for s in open("27-91b.txt"):
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
