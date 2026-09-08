class Solution(object):
    def reverse(self, x):
        int_max = 2**31 - 1
        int_min = - 2**31
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x > 0:
            rem = x % 10
            rev = ( rev*10 ) + rem
            if rev > int_max:
                return 0
            x = x // 10
        return rev*sign
        