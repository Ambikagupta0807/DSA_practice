class Solution:
    def sumOfSeries(self,n):
        #code here
        i = 1
        sum = 0
        while i <= n:
            sum = sum + (i**3)
            i = i+1
        return sum
            