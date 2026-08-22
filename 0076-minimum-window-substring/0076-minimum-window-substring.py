class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if len(t) > len(s):
            return ""
        need = {}
        # Characters required from t
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        left = 0
        right = 0
        required = len(need)
        formed = 0
        min_len = float("inf")
        start = 0
        while right < len(s):
            ch = s[right]
            # Add current character to window
            window[ch] = window.get(ch, 0) + 1
            # Check if this character's required frequency is satisfied
            if ch in need and window[ch] == need[ch]:
                formed += 1
            # Window is valid
            while formed == required:
                # Check if current window is smallest
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                # Remove left character
                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1
            right += 1
        if min_len == float("inf"):
            return ""
        return s[start:start + min_len]