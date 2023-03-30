class Solution(object):
    def isSubsequence(self, s, t):
        # a b c 
        # a h b g d c

        if len(s) == 0:
            return True

        i = 0
        j = 0

        for string in t:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
            if i == len(s):
                return True
        return False


            