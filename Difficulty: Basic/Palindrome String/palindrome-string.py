class Solution:
    def isPalindrome(self, s):
        # code here
        old_s = s
        rev_s = s[::-1]
        if old_s == rev_s:
            return True
        else:
            return False
