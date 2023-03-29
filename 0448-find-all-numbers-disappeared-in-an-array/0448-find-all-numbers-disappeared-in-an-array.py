class Solution(object):
    def findDisappearedNumbers(self, nums):

        res = set(range(1, len(nums)+1))
        nums = set(nums)
        return list(res-nums)
