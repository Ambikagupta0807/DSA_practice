class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        new_str = ""
        for x in s:
            if x.isalnum():
                new_str+=x.lower()
        rev_str = new_str[::-1]

        if new_str == rev_str:
            return True
        else:
            return False

