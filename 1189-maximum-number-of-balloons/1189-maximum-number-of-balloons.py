class Solution(object):
    def maxNumberOfBalloons(self, text):

        letters = {"b": 0 , "a": 0, "l": 0 , "o": 0, "n":0}

        for i in text:
            if i in letters:
                letters[i] += 1
        b = letters.get('b')
        a = letters.get('a')
        l = letters.get('l')
        o = letters.get('o')
        n = letters.get('n')
        return min(b, a, l // 2, o // 2, n)
