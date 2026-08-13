#Find the Smallest Element in an Array
import array 
arr = array.array("i", [23,12,4,6,21])
n = len(arr)
for i in arr:
    print(i, end = " ")
smallest = arr[0]
for i in range (1, n):
    if (arr[i]<smallest):
        smallest = arr[i]
        
print("\n")
print("smallest element is: ", smallest)
    
    