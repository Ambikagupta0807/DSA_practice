#1. Find the Sum of All Elements in an Array
import array
arr = array.array("i", [])
n = int(input("Enter the number of elements you want to store in the array: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))
for i in range (n):
    print(arr[i], end = " ")
print("Sum of all elements: ")
sum = 0
for i in range (0, n):
    sum = sum + arr[i]
    i = i+1
print(sum)