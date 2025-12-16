
start = 12345
end = 13456

count = 0
for n in range(start, end+1):
  s = n*'1'
  while '111' in s:
    s = s.replace('111', '2', 1)
    s = s.replace('222', '11', 1)
    s = s.replace('1', '2', 1)
  #print( n, s )
  count += '1' not in s

print( count )

count = 0
k = start // 16
while 16*k <= end:
  count += start <= 16*k <= end
  count += start <= 16*k+9 <= end
  count += start <= 16*k+10 <= end
  k += 1

print( count )