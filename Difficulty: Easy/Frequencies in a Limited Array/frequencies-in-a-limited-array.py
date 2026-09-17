class Solution:
    def frequencyCount(self, arr):
        #  code here
        n = len(arr)
        count = [0]*n
        for i in arr:
            count[i-1] +=1
        return count