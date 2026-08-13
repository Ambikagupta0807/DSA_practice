def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        currentcard = arr[i]
        j = i-1
        
        while j>=0:
            if arr[j]<currentcard:
                break
            else:
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1] = currentcard
        
    return arr

unsorted_list = [22,11,90,24,34,14]
sorted_list = insertion_sort(unsorted_list)
print("the sorted array is:", sorted_list)