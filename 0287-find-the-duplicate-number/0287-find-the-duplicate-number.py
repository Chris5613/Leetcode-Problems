class Solution(object):
    def findDuplicate(self, nums):
        
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        max_key = max(dict, key=dict.get)
        return max_key