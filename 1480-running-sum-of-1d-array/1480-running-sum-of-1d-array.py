class Solution(object):
    def runningSum(self, nums):
    
        add = 0
        sum = []
        for i in nums:
            add= add+i
            sum.append(add)
        return sum

        