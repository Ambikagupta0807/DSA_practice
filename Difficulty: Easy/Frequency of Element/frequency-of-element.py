class Solution:
    def findFrequency(self, arr, x):
        # code here
        freq = 0
        for i in arr:
            if i == x:
                freq +=1
        return freq