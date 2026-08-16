class Solution(object):
    def maxSubArray(self, nums):
      current_sum = nums[0]
      max_sum = nums[0]
      for x in range(1,len(nums)):
        current_sum = max(nums[x], (nums[x]+current_sum))
        max_sum = max(max_sum, current_sum)
      return max_sum