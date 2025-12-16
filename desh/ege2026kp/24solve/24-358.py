s = open('24-358.txt').readline()

COUNTS = 31

def valid( sub ):
  return sub.count('S') == COUNTS and \
         [p for p in range(len(sub))
            if sub[p] in '02468' ] == [0]

def cantBeValid( sub ):
  return sub.count('S') > COUNTS or \
         sub[0] not in '02468' or \
         [p for p in range(len(sub)) if sub[p] in '02468' ] != [0]

N = len(s)
maxLen = 0
for L in range(N):
  for R in range(L+maxLen+1,N+1):
    sub = s[L:R]
    if valid( sub ):
      maxLen = R - L
      sMax = sub
      print( maxLen, L, R, sMax )
    elif cantBeValid( sub ):
      break

print( maxLen )

# Автор: С. Колхир

from re import *

n = r"[02468]([13579A-RT-Z]*S){31}[13579A-RT-Z]*"
data = finditer(n, s)
ans = []
for x in data:
    ans.append(x.group())
ans.sort(key=lambda x: len(x), reverse=True)
print(len(ans[0])) # 326
print(ans[0]) # Получаем строку которая начинается с 0 (четная цифра) и содержит 31 S и не содержит других четных цифр
print(ans[0].count("0")) # 1
print(ans[0].count("2")) # 0
print(ans[0].count("4")) # 0
print(ans[0].count("6")) # 0
print(ans[0].count("8")) # 0
print(ans[0].count("S")) # 31
print(ans[0] in s)