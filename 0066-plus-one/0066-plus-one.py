class Solution(object):
    def plusOne(self, digits):
        
        string = ""
        for i in digits:
            string += str(i)
        digit = int(string)
        digit = digit + 1 
        result = [int(x) for x in str(digit)]
        return result