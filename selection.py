def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index=j
        arr[i], arr[min_index]= arr[min_index], arr[i]
    return arr

unsorted_list = [22,11,90,24,34,14]
sorted_list = selection_sort(unsorted_list)
print("the sorted array is:", sorted_list)