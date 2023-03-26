class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False

        list = []
        string = str(x)
        for i in string:
            list.append(i)   
        list.reverse()
        new = ""
        for i in list:
            new += i
        return int(new) == x