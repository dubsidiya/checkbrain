# Автор: В. Глезденев

from math import dist

def f_01( x, y ):    # функция распределения по кластерам (+1 аном.)
    d1=dist([x,y],[3,4]); d2=dist([x,y],[10,4])
    if d1<=3.1: return 0
    elif d2<=3.1: return 1
    else: return 2
k = 2  # количество кластеров
klas = [ [] for i in range(k+1) ]     #массив точек по кластерам (+1 - аном.)
for s in open("27-91a.txt"):
    x, y = map(float,s.replace(',','.').split())
    klas[f_01(x,y)].append( (x, y) )
cent = []    # центроиды
for i in range(k): #обработка по кластерам (без ан.)
  mSd = float('inf')  #мин. сум. рас. больше 10**18
  for pC in klas[i]:   # цикл по точкам - центрам
    sumD = sum( dist(pC,p) for p in klas[i] ) # цикл по всем точкам
    if sumD < mSd:
      mSd = sumD; cen = pC
  cent.append( cen ) # сох. цент.
s0=[sum(x) for x in zip(*cent)]
print( int(s0[0]/k*100000), int(s0[1]/k*100000))
