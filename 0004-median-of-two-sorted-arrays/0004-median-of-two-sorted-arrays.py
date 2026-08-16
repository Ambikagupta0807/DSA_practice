class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sorted_lst = []
        x = 0
        y = 0
        while x < len(nums1) and y < len(nums2):
            if nums1[x]<nums2[y]:
                sorted_lst.append(nums1[x])
                x+=1
            else:
                sorted_lst.append(nums2[y])
                y+=1
        while x < len(nums1):
            sorted_lst.append(nums1[x])
            x += 1

        while y < len(nums2):
            sorted_lst.append(nums2[y])
            y += 1

        print(sorted_lst)
        mid = len(sorted_lst)//2

        if len(sorted_lst)%2!=0:
            median = sorted_lst[mid]
            return median
        else:
            median = (sorted_lst[mid-1] + sorted_lst[mid]) / 2.0
            return median

        