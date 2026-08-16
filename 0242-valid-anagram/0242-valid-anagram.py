class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len = len(s)
        t_len = len(t)
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if s_len!=t_len:
            print("Not a anagram")
            return False
        else:
            if sorted_s == sorted_t:
                return True    
            else:
                return False    