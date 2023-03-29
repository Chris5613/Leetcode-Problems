class Solution(object):
    def sortColors(self, nums):

        n = len(nums)
        output = [0] * n

        # Initialize count array
        count = [0] * 10

        # Store the count of each elements in count array
        for i in range(0, n):
            count[nums[i]] += 1

        # Store the cummulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array
        i = n - 1
        while i >= 0:
            output[count[nums[i]] - 1] = nums[i]
            count[nums[i]] -= 1
            i -= 1

        # Copy the sorted elements into original array
        for i in range(0, n):
            nums[i] = output[i]
        
        return nums