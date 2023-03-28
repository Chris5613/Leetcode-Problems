class Solution(object):
    def groupAnagrams(self,strs):
        anagrams = {}
        result = []

        for i in strs:
            sorted_s = ''.join(sorted(i))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(i)
            else:
                anagrams[sorted_s] = [i]
        
        for j in anagrams.values():
            result.append(j)
        
        return result