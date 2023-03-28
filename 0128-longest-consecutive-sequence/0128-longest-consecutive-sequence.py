class Solution(object):
    def longestConsecutive(self, nums):

        hash = set(nums)
        longest = 0

        for num in hash:
            if num - 1 not in hash:
                current = num
                curr_streak = 1

                while current + 1 in hash:
                    current += 1
                    curr_streak += 1

                longest = max(longest, curr_streak)

        return longest

