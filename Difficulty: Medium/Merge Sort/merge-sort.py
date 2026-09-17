class Solution:
    def mergeSort(self, arr, l, r):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        left = self.mergeSort(left, 0, len(left)-1)
        right = self.mergeSort(right, 0, len(right)-1)

        result = self.merge_array(left, right)

        for i in range(len(result)):
            arr[i] = result[i]

        return arr

    def merge_array(self, left, right):
        res = []
        i = 0
        j = 0

        n = len(left)
        m = len(right)

        while i < n and j < m:
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        while i < n:
            res.append(left[i])
            i += 1

        while j < m:
            res.append(right[j])
            j += 1

        return res