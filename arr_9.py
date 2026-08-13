# Check Whether an Element Exists in the Array
import array
arr = array.array("i",[] )
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))
for i in range(n):
    print(arr[i], end = " ")
print("\n")
num = int(input("enter the number you want to search: "))
if num in arr:
    for i in range (n):
        if arr[i]== num:
            print("number exists at index", i)
else:
    print("number doesn't exists in array")
   