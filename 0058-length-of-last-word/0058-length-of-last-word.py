class Solution(object):
    def lengthOfLastWord(self, s):
        
        count = 0
        for i in s[::-1]:
            if i == " ":
                if count >= 1:
                    return count
            else:
                count += 1
        return count
        