def linearsearch(arr,target):
    length = len(arr)
    for index in range(0,length):
        if(target==arr[index]):
            return index
    return -1

arr = [1, 3, 4, 5, 0]
target = int(input("enter target:"))
result = linearsearch(arr, target)
print(result)