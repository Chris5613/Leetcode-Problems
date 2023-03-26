class Solution(object):
    def replaceElements(self, arr):
        n = len(arr)
        max_num = -1
        for i in range(n-1, -1, -1):
            temp = arr[i]
            arr[i] =  max_num
            max_num = max( max_num, temp)
        return arr
