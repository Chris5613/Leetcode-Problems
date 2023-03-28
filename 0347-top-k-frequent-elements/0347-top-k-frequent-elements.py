class Solution(object):
    def topKFrequent(self, nums, k):
        elements = {}
        result = []

        for i in nums:
            if i in elements:
                elements[i] += 1
            else:
                elements[i] = 1
    
        new_dict = sorted(elements.items(),key=lambda x: x[1],reverse =True)
        for i in range(k):
            result.append(new_dict[i][0])
        return result
