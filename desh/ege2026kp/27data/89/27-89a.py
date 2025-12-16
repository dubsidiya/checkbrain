# Автор: В. Глезденев

from math import dist

k = 3  # количество кластеров
klas = [ [] for i in range(k) ]     #массив точек по кластерам
for s in open("27-89a.txt"):
    x, y = map(float,s.replace(',','.').split())
    if y < 6 and x < 8: klas[0].append( (x, y) )
    elif y > x-2: klas[1].append( (x, y) )
    else: klas[2].append( (x, y) )
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
