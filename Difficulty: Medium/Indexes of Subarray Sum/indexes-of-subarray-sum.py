class Solution:
    def subarraySum(self, arr, target):
        start = 0
        total = 0

        for i in range(len(arr)):
            total += arr[i]

            while total > target and start <= i:
                total -= arr[start]
                start += 1

            if total == target:
                return [start + 1, i + 1]

        return [-1]