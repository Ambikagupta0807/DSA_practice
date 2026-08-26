class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        reverse = 0
        while x>0:
            digit = x%10
            reverse = reverse*10 + digit
            x = x//10
        if num == reverse:
            return True
        else:
            return False
