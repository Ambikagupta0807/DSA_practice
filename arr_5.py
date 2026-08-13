#Count Even Numbers in an Array
import array
arr = array.array("i", [])
n = int(input("Enter the number of elements: "))
for i in range(n):
    arr.append(int(input("Enter elements")))
for i in range(n):
    print(arr[i], end = " ")
count = 0
for i in range (n):
    if arr[i]%2==0:
        count = count+1
print("\n")
print("number of even numbers: ", count)