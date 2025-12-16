START = 1
TARGET = 28
MID = 8
NO =  [10, 11]

def nProg( x, target ):
  if x in NO:     # запретные значения
    return False
  if x == target: # если цель достигнута, то
    return 1    # завершить функцию, посчитав цепочку (программу)
  if x > target:  # если перелет, то
      return 0 # завершить функцию, не считая цепочку
  # x < target - продолжаем строить дерево:
  return nProg(x+1, target) + nProg(x+2, target) + nProg(x*3, target)

print( nProg(START, MID) * nProg(MID, TARGET) )

# Динамическое программирование

def si( i ):
  return s[i] if i >= 0 else 0

s = [0]*29
s[1] = 1
for i in range(2,29):
  if i in [10,11]:
    s[i] = 0
  elif i % 3 == 0:
    s[i] = s[i//3] + si(i-1) + si(i-2)
  else:
    s[i] = s[i-1] + s[i-2]
  if i == 8:
    s[:i] = [0]*8

print( s[28] )
