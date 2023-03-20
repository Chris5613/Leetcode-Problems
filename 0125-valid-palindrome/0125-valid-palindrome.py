import re

class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(c for c in s if c.isalnum()).lower()
        return  s[::-1] == s
