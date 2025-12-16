# Автор: А. Сражаев

def div(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: a.update([i,n//i])
    return a

nums = dict()
mn = 0
for n in range(800_001,10**10):
    d = div(n)
    if len(d) not in nums: nums[len(d)] = [n]
    else: nums[len(d)] += [n]
    mn = max(mn,len(nums[len(d)]))
    if mn == 5:
        for x in nums[len(d)]:
            print(x,max(div(x)) ) #, len(d))
        break
