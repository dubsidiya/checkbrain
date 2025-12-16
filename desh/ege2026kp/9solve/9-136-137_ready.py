#136
# нужно проверить, что 360/m = 6
# т.е поворот на внешний угол 60
# проверить, чтобы линия замкнулась
F = open("9-136.txt")
count = 0 
for s in F: 
   k, n, m = map(int,s.split())
   if 360/m == 6 and k>=6:
      count +=1
print(count) 


#137
# пятиугольник, если разность углов 72
# модуль, так как повороты могут быть
# как влево так и вправо

F = open("9-137.txt")
count = 0 
for s in F: 
   k, m, n, x = map(int,s.split())
   if abs(m-x) == 72 and k>=5:
      count +=1
print(count)

