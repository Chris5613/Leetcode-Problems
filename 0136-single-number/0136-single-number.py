class Solution(object):
    def singleNumber(self, nums):

        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        min_key = min(dict, key=dict.get)
        return min_key
