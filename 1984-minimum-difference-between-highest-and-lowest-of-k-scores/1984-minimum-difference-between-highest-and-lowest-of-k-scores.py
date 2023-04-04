class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        l = 0
        r = k-1
        res = float('inf')

        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1

        return res
