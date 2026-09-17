class Solution:
	def reverseSubArray(self,arr,l,r):
		# code here
		left = l-1
		right = r-1
		while left<right:
		    arr[left], arr[right] = arr[right], arr[left]
		    left = left+1
		    right = right - 1
		return arr