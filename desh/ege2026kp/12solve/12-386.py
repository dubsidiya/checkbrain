
start = 12345
end = 14567

count = 0
for n in range(start, end+1):
  s = n*'1'
  while '111' in s:
    s = s.replace('111', '2', 1)
    s = s.replace('222', '11', 1)
    s = s.replace('1', '2', 1)
  #print( n, s )
  count += len(s) == 3

print( count )

count = 0
k = start // 16
while 16*k < end:
  count += start <= 16*k+8 <= end
  count += start <= 16*k+10 <= end
  count += start <= 16*k+13 <= end
  k += 1

print( count )