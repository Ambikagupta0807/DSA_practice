#Find the Largest Element in an Array
import array
arr = array.array("i", [])
n = int(input("Enter the number of elements you want to store in the array: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))
for i in range (n):
    print(arr[i], end = " ")
largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]
        
print("\n")
print("largest element is: ", largest)    
        
    