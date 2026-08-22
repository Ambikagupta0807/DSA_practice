class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        left = 0
        right = n-1
    
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                return mid
                break
            
        return -1