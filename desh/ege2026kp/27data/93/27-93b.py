# Автор: В. Глезденев

from math import dist

k = 3  # количество кластеров
klas = [ [] for i in range(k*2+1) ]     #массив точек по кластерам (+1 аном.)
for s in open("27-93b.txt"):
    x, y = map(float,s.replace(',','.').split())
    if dist([x,y],[9,9])>8: klas[6].append( (x, y) ) # continue
    if y > x+1 and x<9:
        dr=dist([x,y],[5,11])
        if dr<3.1: klas[0].append( (x, y) )
        if dr<0.3: klas[1].append( (x, y) ) #претенденты на центроиды
    if y < x+1 and y<19-x:
        dr=dist([x,y],[9,5])
        if dr<3.1: klas[2].append( (x, y) )
        if dr<0.3: klas[3].append( (x, y) ) #претенденты на центроиды
    if x>9 and y>19-x:
        dr=dist([x,y],[13,11])
        if dr<3.1: klas[4].append( (x, y) )
        if dr<0.3: klas[5].append( (x, y) ) #претенденты на центроиды
cent = []    # центроиды
for i in range(k): #обработка по кластерам (без аном.)
  mSd = float('inf')  #мин. сум. рас. больше 10**18
  for pC in klas[i*2+1]:   # цикл по точкам - центрам из нечет klas
    sumD = sum( dist(pC,p) for p in klas[i*2] ) # цикл по всем точкам из чет klas
    if sumD < mSd:
      mSd = sumD; cen = pC
  cent.append( cen )
s0=[sum(x) for x in zip(*cent)]
print( int(s0[0]/k*100000), int(s0[1]/k*100000) ,len(klas[4]),len(klas[0]))
