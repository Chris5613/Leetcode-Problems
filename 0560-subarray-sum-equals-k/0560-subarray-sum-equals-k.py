class Solution(object):
    def subarraySum(self, nums, k):
        
        # O(N) Solution
        sum_count = {0:1}
        count = 0 
        sum = 0

        for num in nums:
            sum += num
            if sum - k in sum_count:
                count += sum_count[sum-k]
            if sum in sum_count:
                sum_count[sum] += 1
            else:
                sum_count[sum] = 1
        return count


        # O(n^2) Solution

        # count = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             count += 1
        # return count 
