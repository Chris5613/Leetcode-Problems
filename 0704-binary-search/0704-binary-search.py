class Solution(object):
    def search(self, nums, target):
        count = 0 
        for num in nums:
            if num == target:
                return count
            count += 1 
        return -1 