#Print Duplicate Elements
import array
arr = array.array("i",[] )
n = int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))
for i in range(n):
    print(arr[i], end = " ")
print("\n")
count = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i]==arr[j]:
            print(arr[i])
            break

        