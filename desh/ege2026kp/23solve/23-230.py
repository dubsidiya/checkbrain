# Автор: М. Байрамгулов

start = 5001
end = 45789
a = [[0] * 4 for _ in range(end+1)]
a[start][0] = 1
for i in range(start, len(a)):
    if i + 1 <= end:
        a[i+1][0] += a[i][0] - a[i][1]
        a[i+1][1] += a[i][0] - a[i][1]
    if i * 2 <= end:
        a[i*2][0] += a[i][0] - a[i][2]
        a[i*2][2] += a[i][0] - a[i][2]
    if i + 3 <= end:
        a[i+3][0] += a[i][0] - a[i][3]
        a[i+3][3] += a[i][0] - a[i][3]
print( a[end][0] )
# 543131409