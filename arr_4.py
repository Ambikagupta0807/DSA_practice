#Reverse an Array
import array
arr = array.array("i", [])
n = int(input("Enter the number of elements you want to store in the array: "))
for i in range (n):
    arr.append(int(input("Enter the elements")))
for i in arr:
    print(i, end = " ")
print("\n")
for i in arr:
    rev = arr[::-1]
print(rev)
