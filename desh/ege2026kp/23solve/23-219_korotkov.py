# Коротков Михаил Сергеевич
# vk.com/mskorotkov

from math import inf

target = 9217
ones = 30

dp = [[inf] * (ones + 1) for _ in range(target + 1)]
dp[1][0] = 0

for x in range(1, target + 1):
    for k in range(ones + 1):
        length = dp[x][k]

        if length != inf:
            if (x + 1 <= target) and (k + 1 <= ones):
                dp[x + 1][k + 1] = min(dp[x + 1][k + 1], length + 1)

            if x * 2 <= target:
                dp[x * 2][k] = min(dp[x * 2][k], length + 1)

            if x * 3 <= target:
                dp[x * 3][k] = min(dp[x * 3][k], length + 1)

print(dp[target][ones])
