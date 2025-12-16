data = [int(x) for x in open('17-411.txt')]
n = len(data)
mx1 = max(x for x in data if x % 10 == 3)
cnt = 0
mn = float('inf')
for i in range(n-3):
    sm = [ x for x in data[i:i+4] if x % 10 == 2 ]
    if len(sm) % 2 == 1 and max(data[i:i+4]) < mx1:
        cnt += 1
        mn = min( mn, sum(sm) )
print(cnt, mn)

