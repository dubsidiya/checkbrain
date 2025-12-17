# Автор: Д. Козлов

f = open('27-178b.txt')
n = int(f.readline())
nums = [int(x) for x in f]
totalSum = sum(nums)
currSum = maxSum = curr_minSum = minSum = nums[0]
for i in range(1, n):
    currSum = max(currSum + nums[i], nums[i])
    maxSum = max(maxSum, currSum)
    curr_minSum = min(curr_minSum + nums[i], nums[i])
    minSum = min(minSum, curr_minSum)
if (totalSum != minSum):
    print(max(totalSum - minSum, maxSum))
else:
    print(maxSum)
f.close()
# 2109 652822