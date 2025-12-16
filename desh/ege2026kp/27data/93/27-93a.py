# Автор: В. Глезденев

from math import dist

def f_01( x, y ):    # функция распределения по кластерам (+1 аном.)
    d1=dist([x,y],[1.1,5.9])
    d2=dist([x,y],[1.75,2.25])
    if (x<1.1 or y > 5.9) and d1<2.95: return 0
    elif (x>1.75 or y < 2.25) and d2<2.35: return 1
    else: return 2
k = 2  # количество кластеров
klas = [ [] for i in range(k+1) ]     #массив точек по кластерам (+1 аном.)
for s in open("27-93a.txt"):
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
