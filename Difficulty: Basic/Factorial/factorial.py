class Solution:
    def factorial(self, n: int) -> int:
        # code here
        facto = 1
        if n == 1 or n == 0:
            return 1
        facto = n*self.factorial(n-1)
        return facto