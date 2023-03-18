class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dictS = {x: 0 for x in s}
        dictT = {x: 0 for x in t}
        for i in s:
            if i in dictS:
                dictS[i] += 1
        for a in t:
            if a in dictS:
                dictT[a] += 1
        return dictS == dictT