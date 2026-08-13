#Sort the Array in Ascending Order (Without sort())
import array
arr = array.array("i", [])
n = int(input("Enter the no. of elements you want to store in the array: "))
for i in range(n):
    arr.append(int(input("Enter the elements: ")))
print("The array is: ")
print("\n")
for i in range(n):
    print(arr[i], end = " ")
for i in range(n):
    for j in range(i+1, n):
        if arr[i]>arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("The sorted array is : ")
print("\n")
for i in range(n):
    print(arr[i], end = " ")