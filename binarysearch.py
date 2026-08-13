def binarysearch(arr, target):
    length = len(arr)
    p = 0
    q = length -1
    while p<=q:
        mid = (p+q)//2
        if (target == arr[mid]):
            print("tareget found at:" , mid)
            return mid
        elif(target<arr[mid]):
            q = mid-1
        else:
            p = mid+1    
    return -1





sorted_array = [2, 4, 11, 15, 26, 30, 35, 40]
target = 30
result = binarysearch(sorted_array, target)
print (result)