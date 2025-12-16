# Автор: В. Глезденев

from math import dist

def f_01( x, y ):    # функция распределения по кластерам (+1 аном.)
    if y > -2/3*x and y <2/3*x: return 0
    elif y > 3/2*x and y >-3/2*x: return 1
    elif y < -2/3*x and y >2/3*x: return 2
    elif y < -3/2*x and y <3/2*x: return 3
    else: return 4
k = 4  # количество кластеров
klas = [ [] for i in range(k+1) ]     #массив точек по кластерам (+1 аном.)
for s in open("27-90b.txt"):
    x, y = map(float, s.replace(',','.').split())
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
