# Автор: Д. Козлов

f = open('27-177b.txt')
n = int(f.readline())
nums = [int(x) for x in f]

nums1, nums2 = nums[:-1], nums[1:n]
max_prev1, max_prev2 = nums1[0], nums2[0]
for i in range(2, n - 1):
    nums1[i] = max_prev1 + nums1[i]
    max_prev1 = max(max_prev1, nums1[i - 1])
    nums2[i] = max_prev2 + nums2[i]
    max_prev2 = max(max_prev2, nums2[i - 1])
print(max(nums1[n - 2], nums1[n - 3], nums2[n - 2], nums2[n - 3]))
